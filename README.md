# Proyecto CI/CD con GitHub Actions y Docker  
Autor: Miguel Sosa  
Repositorio: https://github.com/MigueSaint/devopsquintoamsg

Este proyecto implementa un flujo completo de Integración Continua (CI) y Entrega Continua (CD) utilizando GitHub Actions, Docker y GitHub Container Registry (GHCR). 
La aplicación está desarrollada en Python con Flask e incluye un formulario web profesional usando Bootstrap.

El proyecto incluye:
- Aplicación funcional en Flask corriendo en el puerto 80  
- Pipeline automatizado con GitHub Actions  
- Construcción y publicación automática de imagen Docker  
- Archivos de despliegue con Docker Swarm y Traefik  
- Manejo de dependencias mediante `requirements.txt`  
- Makefile para facilitar tareas de build y deploy  

---

## 1. Explicación detallada del ciclo CI/CD

El ciclo CI/CD en este proyecto está diseñado para automatizar las tareas esenciales de integración y despliegue. La secuencia es la siguiente:

### 1. Desarrollo y Commit  
Se actualiza o modifica el código de la aplicación en Python (archivo `app.py`), los archivos de configuración o dependencias. 
Al ejecutar un commit y un push a la rama `main`, se activa automáticamente el flujo de trabajo CI/CD.

### 2. Ejecución de GitHub Actions (CI)  
GitHub Actions detecta el push y ejecuta el archivo `.github/workflows/miguel.yml`.  
El workflow realiza los siguientes pasos:

1. Checkout del repositorio.
2. Autenticación con GitHub Container Registry utilizando `GITHUB_TOKEN`.
3. Construcción de la imagen Docker basada en el archivo `Dockerfile`.
4. Publicación del artefacto Docker en GHCR con la etiqueta:  
   `ghcr.io/miguesaint/devopsquintoamsg:1.0.0`

Esto representa el proceso de Integración Continua de manera completa.

### 3. Entrega Continua (CD)  
Una vez que la imagen es publicada en GHCR, es posible utilizarla directamente en un entorno de producción o en un clúster Docker Swarm, como se ejemplifica con el archivo `stack.yml`.

La imagen generada puede ser ejecutada en cualquier servidor con Docker, permitiendo una entrega continua sin intervención manual adicional.

---

## 2. Configuración del CI/CD (Workflow funcional)

Archivo: `.github/workflows/miguel.yml`

```yaml
name: MS Docker image

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    permissions:
      contents: read
      packages: write 

    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Log in to GitHub Container Registry
        uses: docker/login-action@v2
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Build and push Docker image
        uses: docker/build-push-action@v4
        with:
          context: .
          push: true
          tags: ghcr.io/${{ github.actor }}/devopsquintoamsg:1.0.0
