SE LAB (23CTB40B) - ALL CODES, EXPERIMENTS 1-6
Setup once:  pip install pytest pytest-cov

Exp1_SRS               - no code (SRS is a document; see study guide)
Exp2_UseCase           - PlantUML use case diagrams: online shopping, ATM, banking
Exp3_Activity_Class    - PlantUML: library class (manual), library borrowing activity,
                         ATM withdrawal activity, online shopping class
Exp4_WhiteBox_BlackBox - registration_validator.py (manual form) + tests (EP, BVA, 8 paths)
                         login_validator.py + tests (V(G)=6), cyclomatic_complexity.py
Exp5_TestCases         - calculator.py + test_calculator.py (all 28 ADD/SUB/MUL/DIV cases)
                         triangle.py + test_triangle.py (EP + BVA)
Exp6_UnitTesting       - grade_calculator.py + tests (manual), bank_account.py + tests,
                         string_utils.py + tests, java/ (JUnit 5 example)

Run tests inside each folder:
  cd Exp6_UnitTesting
  pytest -v
  pytest -v --cov=grade_calculator --cov-report=term-missing
Run calculator interactively:  python calculator.py
Diagrams: paste .puml text into https://www.plantuml.com/plantuml
JUnit: needs junit-jupiter jar (or run in IntelliJ/Eclipse/Maven project).
