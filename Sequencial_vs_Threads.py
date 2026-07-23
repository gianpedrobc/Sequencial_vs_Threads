import threading, time, urllib.request
from datetime import datetime

# Função que pega a hora exata para mostrar na tela
def hora_atual():
    return datetime.now().strftime("%H:%M:%S")

def baixar_arquivo(url, nome_do_arquivo):
    print(f"[{hora_atual()}] {nome_do_arquivo} -> Iniciando o download...")
    
    # A thread "para" (bloqueia) nesta linha enquanto espera a internet
    urllib.request.urlretrieve(url, nome_do_arquivo)
    
    print(f"[{hora_atual()}] {nome_do_arquivo} -> Download concluído!")

def main():
    # URLs de imagens pesadas para dar tempo de ver a diferença
    url1 = "https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0?q=80&w=3000"
    url2 = "https://images.unsplash.com/photo-1472214103451-9374bd1c798e?q=80&w=3000"

    print("==================================================")
    print("      TESTE 1: MODO SEQUENCIAL (Sem Threads)      ")
    print("==================================================")
    inicio_seq = time.time()
    
    # Um tem que terminar para o outro começar
    baixar_arquivo(url1, "imagem_A_seq.jpg")
    baixar_arquivo(url2, "imagem_B_seq.jpg")
    
    tempo_seq = time.time() - inicio_seq
    print(f"\n[RESULTADO] Tempo Sequencial: {tempo_seq:.2f} segundos\n")


    print("==================================================")
    print("      TESTE 2: MODO CONCORRENTE (Com Threads)     ")
    print("==================================================")
    inicio_thread = time.time()
    
    # Criamos as threads
    t1 = threading.Thread(target=baixar_arquivo, args=(url1, "imagem_A_thread.jpg"))
    t2 = threading.Thread(target=baixar_arquivo, args=(url2, "imagem_B_thread.jpg"))

    # Damos a largada juntas
    t1.start()
    t2.start()

    # Esperamos as duas terminarem
    t1.join()
    t2.join()
    
    tempo_thread = time.time() - inicio_thread
    print(f"\n[RESULTADO] Tempo com Threads: {tempo_thread:.2f} segundos\n")


    print("==================================================")
    print("                    CONCLUSÃO                     ")
    print("==================================================")
    economia = tempo_seq - tempo_thread
    print(f"Usar Threads economizou {economia:.2f} segundos!")

if __name__ == "__main__":
    main()