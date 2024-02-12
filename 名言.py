import MeCab
import markovify

mecab = MeCab.Tagger("-Owakati")

print("素材のファイル(txtファイルの)絶対パスを入れてください")
fail_url = input()
fail_url_sp = fail_url+'-splitted.txt'

inputb = open(fail_url, 'r', encoding='utf-8')
output = open(fail_url_sp, 'w', encoding='utf-8')

for line in inputb.read().split('\n'):
	splittedLine = ' '.join(mecab.parse(line).split())
	output.write(splittedLine)
	output.write('\n')
      
inputb.close()
output.close()

print("何個名言を作りますか？")
number = int(input())

for i in range(number):
    inputa = open(fail_url_sp ,'r', encoding='utf-8')
    model = markovify.NewlineText(inputa.read())
    sentence = model.make_sentence()
    print(sentence.replace(" ",""))

inputa.close()