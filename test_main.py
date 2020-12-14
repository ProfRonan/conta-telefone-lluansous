"""Esse módulo é utilizado para realizar testes automáticos dos exercícios."""

import unittest
from unittest.mock import patch
import main


class Test(unittest.TestCase):
    """Classe para agregar os métodos que serão utilizados para testar."""
    def test_less_100(self):
        """Função que testa valor < 100."""
        # Lista de valores que serão retornados pela função input.
        input_returns = [63]
        input_returns = map(str, input_returns)
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            mock_print.assert_called_with('O valor devido é R$ 200.00.')

    def test_100(self):
        """Função que testa valor = 100."""
        # Lista de valores que serão retornados pela função input.
        input_returns = [100]
        input_returns = map(str, input_returns)
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            mock_print.assert_called_with('O valor devido é R$ 200.00.')

    def test_greater_100(self):
        """Função que testa valor > 100."""
        # Lista de valores que serão retornados pela função input.
        input_returns = [143]
        input_returns = list(map(str, input_returns))
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            mock_print.assert_called_with('O valor devido é R$ 225.80.')

    def test_greater_150(self):
        """Função que testa valor > 150."""
        # Lista de valores que serão retornados pela função input.
        input_returns = [153]
        input_returns = map(str, input_returns)
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            mock_print.assert_called_with('O valor devido é R$ 231.50.')

    def test_greater_200(self):
        """Função que testa valor > 200."""
        # Lista de valores que serão retornados pela função input.
        input_returns = [253]
        input_returns = map(str, input_returns)
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            mock_print.assert_called_with('O valor devido é R$ 276.20.')


if __name__ == '__main__':
    unittest.main()
