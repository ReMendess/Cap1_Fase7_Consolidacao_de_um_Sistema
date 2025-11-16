# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import webbrowser

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system("cls" if os.name == "nt" else "clear")

def verificar_arquivo(nome_arquivo):
    """Verifica se o arquivo existe no diretório atual"""
    return os.path.isfile(nome_arquivo)

def executar_aplicacao(nome_arquivo):
    """Executa a aplicação Python especificada"""
    try:
        limpar_tela()
        print(f"\n{'='*50}")
        print(f"Iniciando: {nome_arquivo}")
        print(f"{'='*50}\n")
        
        # Executa o arquivo Python
        subprocess.run([sys.executable, nome_arquivo])
        
        print(f"\n{'='*50}")
        print(f"Aplicação '{nome_arquivo}' finalizada")
        print(f"{'='*50}")
        input("\nPressione ENTER para voltar ao menu principal...")
        
    except FileNotFoundError:
        print(f"\nERRO: Arquivo '{nome_arquivo}' não encontrado!")
        print("Certifique-se de que o arquivo está no mesmo diretório.")
        input("\nPressione ENTER para continuar...")
    except Exception as e:
        print(f"\nERRO ao executar '{nome_arquivo}': {e}")
        input("\nPressione ENTER para continuar...")

def abrir_streamlit():
    """Abre a aplicação Streamlit no navegador"""
    url = "https://fase4cap1automintelig-n3hqyyxxjbmt2qtkguk38y.streamlit.app"
    try:
        limpar_tela()
        print(f"\n{'='*60}")
        print("Abrindo aplicação Streamlit no navegador...")
        print(f"{'='*60}")
        print(f"\nURL: {url}")
        print("\nSe o navegador não abrir automaticamente,")
        print("copie e cole o link acima no seu navegador.")
        print(f"\n{'='*60}")
        
        webbrowser.open(url)
        print("\n✓ Navegador aberto com sucesso!")
        input("\nPressione ENTER para voltar ao menu principal...")
        
    except Exception as e:
        print(f"\nERRO ao abrir navegador: {e}")
        print(f"\nAcesse manualmente: {url}")
        input("\nPressione ENTER para continuar...")

def abrir_notebook():
    """Abre o notebook Jupyter"""
    nome_notebook = "Fase4_Scikit_Learn.ipynb"
    try:
        limpar_tela()
        print(f"\n{'='*60}")
        print("Abrindo Jupyter Notebook...")
        print(f"{'='*60}\n")
        
        if not verificar_arquivo(nome_notebook):
            print(f"⚠ AVISO: Arquivo '{nome_notebook}' não encontrado!")
            print("\nCertifique-se de que o arquivo está no diretório atual.")
            input("\nPressione ENTER para continuar...")
            return
        
        # Tenta abrir com Jupyter Notebook
        try:
            subprocess.Popen(["jupyter", "notebook", nome_notebook])
            print(f"✓ Jupyter Notebook iniciado!")
            print(f"✓ Abrindo: {nome_notebook}")
            print("\nO notebook será aberto no seu navegador.")
            print("\nPara encerrar o servidor Jupyter, feche a janela do terminal")
            print("que foi aberta ou pressione Ctrl+C nela.")
            
        except FileNotFoundError:
            # Se jupyter não estiver no PATH, tenta com python -m
            subprocess.Popen([sys.executable, "-m", "notebook", nome_notebook])
            print(f"✓ Jupyter Notebook iniciado!")
            print(f"✓ Abrindo: {nome_notebook}")
        
        print(f"\n{'='*60}")
        input("\nPressione ENTER para voltar ao menu principal...")
        
    except Exception as e:
        print(f"\nERRO ao abrir notebook: {e}")
        print("\nVerifique se o Jupyter está instalado:")
        print("  pip install notebook")
        print(f"\nOu abra manualmente com: jupyter notebook {nome_notebook}")
        input("\nPressione ENTER para continuar...")

def abrir_notebook_visao():
    """Abre o notebook de Visão Computacional"""
    nome_notebook = "Fase_6.ipynb"
    try:
        limpar_tela()
        print(f"\n{'='*60}")
        print("Abrindo Jupyter Notebook - Visão Computacional...")
        print(f"{'='*60}\n")
        
        if not verificar_arquivo(nome_notebook):
            print(f"⚠ AVISO: Arquivo '{nome_notebook}' não encontrado!")
            print("\nCertifique-se de que o arquivo está no diretório atual.")
            input("\nPressione ENTER para continuar...")
            return
        
        # Tenta abrir com Jupyter Notebook
        try:
            subprocess.Popen(["jupyter", "notebook", nome_notebook])
            print(f"✓ Jupyter Notebook iniciado!")
            print(f"✓ Abrindo: {nome_notebook}")
            print("\n📸 Notebook de Visão Computacional com YOLO")
            print("\nO notebook será aberto no seu navegador.")
            print("\nPara encerrar o servidor Jupyter, feche a janela do terminal")
            print("que foi aberta ou pressione Ctrl+C nela.")
            
        except FileNotFoundError:
            # Se jupyter não estiver no PATH, tenta com python -m
            subprocess.Popen([sys.executable, "-m", "notebook", nome_notebook])
            print(f"✓ Jupyter Notebook iniciado!")
            print(f"✓ Abrindo: {nome_notebook}")
        
        print(f"\n{'='*60}")
        input("\nPressione ENTER para voltar ao menu principal...")
        
    except Exception as e:
        print(f"\nERRO ao abrir notebook: {e}")
        print("\nVerifique se o Jupyter está instalado:")
        print("  pip install notebook")
        print(f"\nOu abra manualmente com: jupyter notebook {nome_notebook}")
        input("\nPressione ENTER para continuar...")

def exibir_menu():
    """Exibe o menu principal"""
    limpar_tela()
    print("\n" + "="*60)
    print(" "*15 + "MENU PRINCIPAL DO SISTEMA")
    print("="*60)
    print("\n[1] Fase 1 & 2 - Banco de Dados")
    print("    → Gerenciamento de sensores (pH, Fósforo, Potássio)")
    print("\n[2] Fase 3 - IoT")
    print("    → Gerenciamento completo de sensores + Exportação CSV")
    print("    → (pH, Fósforo, Potássio, Temperatura, Umidade)")
    print("\n[3] API Meteorológica")
    print("    → Consulta de previsão do tempo e status de irrigação")
    print("\n[4] Fase 4 - Aplicação Streamlit (Web)")
    print("    → Análise e predição de dados (online)")
    print("\n[5] Fase 5 - Notebook de Treinamento")
    print("    → Treinamento de modelos com Scikit-Learn")
    print("\n[6] Fase 6 - Visão Computacional com Redes Neurais")
    print("    → Sistema de monitoramento visual com YOLO")
    print("\n[7] Informações do Sistema")
    print("\n[0] Sair")
    print("\n" + "="*60)

def exibir_informacoes():
    """Exibe informações sobre o sistema"""
    limpar_tela()
    print("\n" + "="*60)
    print(" "*15 + "INFORMAÇÕES DO SISTEMA")
    print("="*60)
    print("\nSistema de Monitoramento Agrícola")
    print("\nMódulos disponíveis:")
    print("  • Fase 1 & 2: CRUD básico de sensores no Oracle DB")
    print("  • Fase 3: CRUD expandido + exportação de dados")
    print("  • API Meteorológica: Previsão do tempo e irrigação")
    print("  • Fase 4 Web: Aplicação Streamlit de análise e predição")
    print("  • Fase 5 ML: Notebook de treinamento de modelos")
    print("  • Fase 6 CV: Visão computacional com YOLO")
    print("\nArquivos necessários:")
    
    arquivos = [
        "Fase1&2Banco_de_dados.py",
        "Fase3_IOT.py",
        "API_Metereologica.py",
        "Fase4_Scikit_Learn.ipynb",
        "Fase_6.ipynb"
    ]
    
    print()
    for arquivo in arquivos:
        status = "✓ Encontrado" if verificar_arquivo(arquivo) else "✗ NÃO ENCONTRADO"
        print(f"  {status}: {arquivo}")
    
    print("\n" + "="*60)
    input("\nPressione ENTER para voltar...")

def menu_principal():
    """Loop principal do menu"""
    aplicacoes = {
        1: "Fase1&2Banco_de_dados.py",
        2: "Fase3_IOT.py",
        3: "API_Metereologica.py"
    }
    
    while True:
        exibir_menu()
        
        try:
            opcao = int(input("\nEscolha uma opção: "))
            
            if opcao == 0:
                limpar_tela()
                print("\n" + "="*60)
                print("Encerrando o sistema...")
                print("Obrigado por utilizar o Sistema de Monitoramento!")
                print("="*60 + "\n")
                sys.exit(0)
            
            elif opcao == 4:
                abrir_streamlit()
            
            elif opcao == 5:
                abrir_notebook()
            
            elif opcao == 6:
                abrir_notebook_visao()
            
            elif opcao == 7:
                exibir_informacoes()
            
            elif opcao in aplicacoes:
                nome_arquivo = aplicacoes[opcao]
                if verificar_arquivo(nome_arquivo):
                    executar_aplicacao(nome_arquivo)
                else:
                    limpar_tela()
                    print(f"\n{'='*60}")
                    print("ERRO: Arquivo não encontrado!")
                    print(f"{'='*60}")
                    print(f"\nO arquivo '{nome_arquivo}' não está no diretório atual.")
                    print("\nCertifique-se de que todos os arquivos estão na mesma pasta:")
                    print(f"  • {nome_arquivo}")
                    print(f"  • {os.path.basename(__file__)}")
                    print(f"\n{'='*60}")
                    input("\nPressione ENTER para continuar...")
            
            else:
                limpar_tela()
                print("\n⚠ Opção inválida! Escolha um número entre 0 e 7.")
                input("Pressione ENTER para continuar...")
        
        except ValueError:
            limpar_tela()
            print("\n⚠ Entrada inválida! Digite apenas números.")
            input("Pressione ENTER para continuar...")
        except KeyboardInterrupt:
            limpar_tela()
            print("\n\nOperação cancelada pelo usuário.")
            print("Até logo!\n")
            sys.exit(0)

if __name__ == "__main__":
    try:
        menu_principal()
    except Exception as e:
        print(f"\n\nERRO CRÍTICO: {e}")
        print("O sistema será encerrado.")
        input("\nPressione ENTER para sair...")
        sys.exit(1)