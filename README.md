# mi_super_bot

## Ambiente de Desarrollo

Configurar un ambiente virtual de python

```ps
PS > python -m venv venv
PS > .\venv\Scripts\Activate.ps1
PS > (venv) python -m pip install --upgrade pip
PS > (venv) pip install -r requirements.txt
```

Crear archivo de configuración

```env
# src/frontend_telegram/.env

TELEGRAM_TOKEN=
```

Ejecutar bot
```env
PS src/frontend_telegram/> (venv) python main.py
```