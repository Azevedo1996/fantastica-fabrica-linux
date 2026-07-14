from django import forms

PHASE_CHOICES = (
    (1, 'Fase 1 — A Visita à Fábrica'),
    (2, 'Fase 2 — A Mão na Massa'),
    (3, 'Fase 3 — Os Sabores da Fábrica'),
    (4, 'Fase 4 — O Elevador de Vidro'),
)

class StartGameForm(forms.Form):
    player_name = forms.CharField(label='Nome do visitante', max_length=80, required=False)
    selected_phase = forms.ChoiceField(label='Escolha a fase', choices=PHASE_CHOICES, initial=1)

class AnswerForm(forms.Form):
    answer = forms.CharField(label='Resposta', max_length=255, widget=forms.TextInput(attrs={
        'placeholder': 'Digite o comando ou conceito...',
        'autocomplete': 'off',
        'autofocus': 'autofocus',
        'class': 'terminal-input',
    }))
