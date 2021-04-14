class Bug:
    language = ""

    def __init__(self, bug_id, characteristics, test_case_correct, symptom,
                 root_cause, category, lines=0):
        self.bug_id = bug_id
        self.characteristics = characteristics
        self.test_case_correct = test_case_correct
        self.symptom = symptom
        self.root_cause = root_cause
        self.category = category
        self.lines = 0 # test case loc

    def __repr__(self):
        return "Bug: {} (\n\t{}\n\t{}\n\t{}\n\t{}\n\t{}\n\t{}\n)".format(
            self.bug_id,
            "Characteristics: \n\t\t" + "\n\t\t".join([str(c) for c in self.characteristics]),
            "Test Case Correct: " + str(self.test_case_correct),
            "Symptom: " + str(self.symptom),
            "Root Cause: " + str(self.root_cause),
            "Category: " + str(self.category),
            "Test case loc: " + str(self.lines)
        )

    def __str__(self):
        return self.__repr__()


class KotlinBug(Bug):
    language = "Kotlin"
    compiler = "kotlinc"


class GroovyBug(Bug):
    language = "Groovy"
    compiler = "groovyc"


class JavaBug(Bug):
    language = "Java"
    compiler = "javac (openjdk)"


class ScalaBug(Bug):
    language = "Scala"
    compiler = "scala"


class ScalaDottyBug(ScalaBug):
    compiler = "dotty"
