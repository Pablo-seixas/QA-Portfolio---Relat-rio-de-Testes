import xml.etree.ElementTree as ET

tree = ET.parse('../../evidence/pytest/pytest_run_01.xml')
root = tree.getroot()

# Pega o primeiro testsuite
testsuite = root.find('testsuite')

with open('../../evidence/pytest/pytest_run_01.md', 'w') as f:
    f.write("# Relatório Pytest - QA Portfolio\n\n")
    f.write(f"Total de testes: {testsuite.attrib.get('tests', 'N/A')}\n")
    f.write(f"Falhas: {testsuite.attrib.get('failures', 'N/A')}\n")
    f.write(f"Erros: {testsuite.attrib.get('errors', 'N/A')}\n")
    f.write(f"Pulados: {testsuite.attrib.get('skipped', 'N/A')}\n\n")

    for testcase in testsuite.findall('testcase'):
        name = testcase.attrib.get('name', 'N/A')
        time = testcase.attrib.get('time', 'N/A')
        status = 'PASS'
        if testcase.find('failure') is not None:
            status = 'FAIL'
        elif testcase.find('error') is not None:
            status = 'ERROR'
        f.write(f"- {name} | {status} | {time}s\n")
