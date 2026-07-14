
from django.db import models
from django.contrib.auth.models import User

class Mission(models.Model):
    phase = models.PositiveIntegerField('Fase', default=1)
    order = models.PositiveIntegerField('Ordem', default=1)
    title = models.CharField('Título', max_length=160)
    story = models.TextField('História')
    question = models.TextField('Pergunta')
    expected_answer = models.CharField('Resposta esperada', max_length=160)
    aliases = models.CharField('Respostas aceitas', max_length=350, blank=True, help_text='Separe por vírgula.')
    command_example = models.CharField('Exemplo de comando', max_length=220, blank=True)
    explanation = models.TextField('Explicação')
    reward = models.CharField('Recompensa da missão', max_length=160, blank=True)
    points = models.PositiveIntegerField('Pontos', default=10)

    class Meta:
        ordering = ['phase', 'order']
        unique_together = ('phase', 'order')
        verbose_name = 'Missão'
        verbose_name_plural = 'Missões'

    def __str__(self):
        return f'Fase {self.phase} - {self.order}. {self.title}'

    def accepted_answers(self):
        values = [self.expected_answer]
        if self.aliases:
            values.extend([a.strip() for a in self.aliases.split(',') if a.strip()])
        return [v.lower().strip() for v in values]

class PlayerSession(models.Model):
    player_name = models.CharField('Nome do visitante', max_length=80, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    selected_phase = models.PositiveIntegerField(default=1)
    current_mission = models.PositiveIntegerField(default=1)
    score = models.PositiveIntegerField(default=0)
    rewards = models.TextField('Recompensas coletadas', blank=True)
    finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Sessão do jogador'
        verbose_name_plural = 'Sessões dos jogadores'

    def __str__(self):
        return f'{self.player_name or "Visitante"} - Fase {self.selected_phase}'

    def add_reward(self, reward):
        if not reward:
            return
        current = [r for r in self.rewards.split('\n') if r.strip()]
        if reward not in current:
            current.append(reward)
            self.rewards = '\n'.join(current)

    def reward_list(self):
        return [r for r in self.rewards.split('\n') if r.strip()]

class AnswerLog(models.Model):
    session = models.ForeignKey(PlayerSession, on_delete=models.CASCADE, related_name='answers')
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
