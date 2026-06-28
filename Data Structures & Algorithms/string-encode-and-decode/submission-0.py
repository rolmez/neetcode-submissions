class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for word in strs:
            encoded += f'{len(word)}#{word}'
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = s.find("#", i)          # 1) '#' bul
            length = int(s[i:j])        # 2) uzunluğu oku
            start = j + 1               # 3) kelimenin başlangıcı
            end = start + length        # 4) kelimenin bitişi

            word = s[start:end]         # 5) kelimeyi al
            res.append(word)

            i = end                     # 6) pointer'ı ileri taşı

        return res