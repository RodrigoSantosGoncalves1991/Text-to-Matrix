
# Text-to-Matrix

Arquivo txt é lido, os caracteres "\n" de quebra de linha são substituitos por um espaço 
" " por meio do método replace(), depois a string que representa o texto é desmembrada em 
elementos de uma matrix (array) através do método split(). Com esses dados brutos é feita 
uma filtragem e de caracteres de pontuação e uma série de contagens para obter um histograma 
com as probabilidades da 20 palavras com mais ocorrências no texto. E por fim os dados brutos 
em array são concatenados em uma string e transformados em um arquivo de texto novamente.
