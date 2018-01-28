# coding=utf-8
from unittest import TestCase
from click.testing import CliRunner

import yoda


class TestSpeedtest(TestCase):
    """
        Test for the following commands:

        | Module: dev
        | command: url
    """

    def __init__(self, methodName='runTest'):
        super(TestSpeedtest, self).__init__()
        self.runner = CliRunner()

    def runTest(self):
        def test_word():
            result = self.runner.invoke(yoda.cli, ['vocabulary', 'word'], input='\nn')
            self.assertEqual(0, result.exit_code)
            output_string = str(result.output.encode('ascii', 'ignore'))

            self.assertEqual(type(output_string), str)

        def test_accuracy():
            result = self.runner.invoke(yoda.cli, ['vocabulary', 'accuracy'])
            self.assertEqual(0, result.exit_code)
            output_string = str(result.output.encode('ascii', 'ignore'))

            self.assertEqual(type(output_string), str)

        test_word()
        test_accuracy()