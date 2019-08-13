from context import meta
import unittest
import mock


class AdvancedTestSuite(unittest.TestCase):


    def test_post(self):
        dna = {"dna": ""["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]""}
#       resp = requests.post(config.tool_repo_urls['es_url'], data=json.dumps(info), headers={'Content-Type': 'application/json'})
#        assert_equal(resp.status_code, 200)#, "Metahuman"
       
        headers = {
            'ContentType': 'application/json',
            'dataType': 'json'
        }


        response = self.test_app.post('/metahuman',
                                      data=json.dumps(dna),
                                      content_type='application/json',
                                      follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))


if __name__ == '__main__':
    unittest.main()
