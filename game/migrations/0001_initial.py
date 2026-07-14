from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phase', models.PositiveIntegerField(default=1, verbose_name='Fase')),
                ('order', models.PositiveIntegerField(default=1, verbose_name='Ordem')),
                ('title', models.CharField(max_length=160, verbose_name='Título')),
                ('story', models.TextField(verbose_name='História')),
                ('question', models.TextField(verbose_name='Pergunta')),
                ('expected_answer', models.CharField(max_length=160, verbose_name='Resposta esperada')),
                ('aliases', models.CharField(blank=True, help_text='Separe por vírgula.', max_length=350, verbose_name='Respostas aceitas')),
                ('command_example', models.CharField(blank=True, max_length=220, verbose_name='Exemplo de comando')),
                ('explanation', models.TextField(verbose_name='Explicação')),
                ('reward', models.CharField(blank=True, max_length=160, verbose_name='Recompensa da missão')),
                ('points', models.PositiveIntegerField(default=10, verbose_name='Pontos')),
            ],
            options={'verbose_name':'Missão','verbose_name_plural':'Missões','ordering':['phase','order'],'unique_together':{('phase','order')}},
        ),
        migrations.CreateModel(
            name='PlayerSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(blank=True, max_length=80, verbose_name='Nome do visitante')),
                ('selected_phase', models.PositiveIntegerField(default=1)),
                ('current_mission', models.PositiveIntegerField(default=1)),
                ('score', models.PositiveIntegerField(default=0)),
                ('rewards', models.TextField(blank=True, verbose_name='Recompensas coletadas')),
                ('finished', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={'verbose_name':'Sessão do jogador','verbose_name_plural':'Sessões dos jogadores'},
        ),
        migrations.CreateModel(
            name='AnswerLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=255)),
                ('correct', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.mission')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='game.playersession')),
            ],
            options={'ordering':['created_at']},
        ),
    ]
