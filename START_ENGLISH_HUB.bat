@echo off
chcp 65001 >nul
title English Study Hub - Local Server

echo ============================================
echo   English Study Hub - Iniciando Servidor
echo ============================================
echo.

cd /d "%~dp0"

echo Verificando Python...
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Python encontrado! Iniciando servidor na porta 8000...
    echo.
    echo Abrindo no navegador: http://localhost:8000/english-study-hub.html
    echo.
    echo ============================================
    echo   NAO FECHE ESTA JANELA!
    echo   O servidor precisa ficar rodando.
    echo   Pressione Ctrl+C para parar.
    echo ============================================
    echo.
    
    start "" "http://localhost:8000/english-study-hub.html"
    python -m http.server 8000
) else (
    echo Python nao encontrado. Verificando Node.js...
    node --version >nul 2>&1
    if %errorlevel% equ 0 (
        echo Node.js encontrado! Iniciando com npx serve...
        echo.
        echo Abrindo no navegador...
        echo.
        echo ============================================
        echo   NAO FECHE ESTA JANELA!
        echo ============================================
        echo.
        npx serve . -l 8000
    ) else (
        echo.
        echo ERRO: Nem Python nem Node.js estao instalados.
        echo.
        echo SOLUCAO: Instale o Python em https://python.org
        echo (Marque "Add Python to PATH" durante a instalacao)
        echo.
        pause
    )
)