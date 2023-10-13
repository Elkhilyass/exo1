import unittest

def processLines(lines) -> str:
        N=int(lines[0])
        T=int(lines[1])
        backlog = T
        for i in range(2,N+2):
                V,U = map(int, lines[i].split())
                backlog = backlog- V + U
                
                if backlog < 0:
                        return "KO"
                     
        if backlog == 0:
                return "OK"
        else:
                return "KO"

class TestExo3(unittest.TestCase):
    def test_input_1(self):
        with open("exo3/sample/input1.txt") as input1:
            lines = input1.readlines()

        with open("exo3/sample/output1.txt") as output1:
            expected = output1.read()

        self.assertEqual(expected, processLines(lines))
    
    def test_input_2(self):
        with open("exo3/sample/input2.txt") as input2:
            lines = input2.readlines()

        with open("exo3/sample/output2.txt") as output2:
            expected = output2.read()

        self.assertEqual(expected, processLines(lines))


if __name__ == '__main__':
    unittest.main()

    # Ecrire une autre méthode pour vérifier le second use case
