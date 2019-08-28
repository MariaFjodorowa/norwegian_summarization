from baselines.extraction_score import count_extraction_score

def test_extraction_score():
    testarticle = """С точки зрения научной систематики, домашняя кошка — млекопитающее семейства кошачьих отряда хищных.
     Ранее домашнюю кошку нередко рассматривали как отдельный биологический вид.
     С точки зрения современной биологической систематики домашняя кошка (Felis silvestris catus) является подвидом лесной кошки (Felis silvestris)."""

    testsummary1 = 'Домашняя кошка - не отдельный биологический вид. Домашняя кошка (Felis silvestris catus) является подвидом лесной кошки'

    testsummary2 = "Котэ - это зверь из леса."

    testsummary3 = """С точки зрения научной систематики, домашняя кошка — млекопитающее семейства кошачьих отряда хищных.
     Ранее домашнюю кошку нередко рассматривали как отдельный биологический вид.
     С точки зрения современной биологической систематики домашняя кошка (Felis silvestris catus) является подвидом лесной кошки (Felis silvestris)."""

    extraction_score1 = count_extraction_score(testarticle, testsummary1)
    assert (extraction_score1 > 0 and extraction_score1 < 1)
    assert count_extraction_score(testarticle, testsummary2) == 0
    assert count_extraction_score(testarticle, testsummary3) == 1.0






