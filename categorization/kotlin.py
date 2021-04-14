from bug import KotlinBug
import categories as ct
import characteristics as pc
import symptoms as sy
import root_causes as rc


kotlin_iter1 = [
    KotlinBug(
        "1.KT-1934",
        [pc.Inheritance(), pc.MultipleImplements()],
        False,
        sy.Runtime(sy.WrongResult()),
        rc.MissingCase(),
        ct.MissingValiationChecks(),
        4
    ),
    KotlinBug(
        "2.KT-4814",
        [pc.ArithmeticExpressions(), pc.AugmentedAssignmentOperator()],
        False,
        sy.Runtime(sy.VerifyError()),
        rc.MissingCase(),
        ct.IncorrectAnalysisMechanics(),
        4
    ),
    KotlinBug(
        "3.KT-42175",
        [
            pc.Lambdas(),
            pc.Collections(),
            pc.This(),
            pc.AugmentedAssignmentOperator()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Inference(),
        8
    ),
    KotlinBug(
        "4.KT-10244",
        [pc.FlowTyping(),
         pc.Conditionals(),
         pc.ReturnTypeInference()],
        False,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        ct.MissingValiationChecks(),
        4
    ),
    KotlinBug(
        "5.KT-10472",
        [pc.Overloading(), pc.Varargs(),
         pc.ParameterizedClasses(),
         pc.ParameterizedFunctions(),
         pc.TypeArgsInference(),
         pc.Inheritance(),
         pc.ParameterizedTypes()],
        True,
        sy.Runtime(sy.WrongResult()),
        rc.IncorrectSequence(),
        ct.Resolution(),
        8
    ),
    KotlinBug(
        "6.KT-7485",
        [pc.MultiBounds(),
         pc.BoundedPolymorphism(),
         pc.ParameterizedFunctions(),
         pc.Nullables(),
         pc.Subtyping()],
        False,
        sy.Runtime(sy.NullPointerException()),
        rc.IncorrectComputation(),
        ct.TypeComparison(),
        11
    ),
    KotlinBug(
        "7.KT-13401",
        [pc.ParameterizedClasses(),
         pc.BoundedPolymorphism(),
         pc.WildCardType(),
         ],
        True,
        sy.InternalCompilerError(),
        rc.IncorrectCondition(),
        ct.TypeComparison(),
        9
    ),
    KotlinBug(
        "8.KT-22728",
        [pc.Lambdas(),
         pc.ExtensionFunctions(),
         pc.Typedefs(),
         pc.Import(),
         pc.FunctionTypes()],
        True,
        sy.CompileTimeError(),
        rc.WrongParams(),
        ct.Environment(),
        11
    ),
    KotlinBug(
        "9.KT-10711",
        [pc.TypeArgsInference(),
         pc.ParameterizedClasses(),
         pc.Collections(),
         pc.FunctionReferences()],
        True,
        sy.CompileTimeError(),
        rc.InsufficientAlgorithmImplementation(),
        ct.Inference(),
        6
    ),
    KotlinBug(
        "10.KT-37249",
        [pc.Conditionals(), pc.TryCatch(), pc.Lambdas()],
        True,
        sy.CompileTimeError(),
        rc.InsufficientAlgorithmImplementation(),
        ct.Inference(),
        7
    ),
    KotlinBug(
        "11.KT-11468",
        [pc.ParameterizedClasses(), pc.DeclVariance(),
         pc.ParameterizedTypes(),
         pc.Inheritance(), pc.ParameterizedFunctions(),
         pc.WildCardType(),
         pc.TypeArgsInference(), pc.ElvisOperator(),
         pc.Subtyping()],
        True,
        sy.InternalCompilerError(),
        rc.DesignIssue(),
        ct.TypeComparison(),
        6
    ),
    KotlinBug(
        "12.KT-6014",
        [pc.Overriding(), pc.Inheritance(), pc.Delegation()],
        True,
        sy.CompileTimeError(),
        rc.IncorrectComputation(),
        ct.Resolution(),
        7
    ),
    KotlinBug(
        "13.KT-12044",
        [pc.Conditionals(), pc.PropertyReference(), pc.ParameterizedTypes()],
        True,
        sy.CompileTimeError(),
        rc.WrongParams(),
        ct.Resolution(),
        8
    ),
    KotlinBug(
        "14.KT-4334",
        [pc.Lambdas(), pc.Loops(), pc.Collections()],
        False,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        ct.MissingValiationChecks(),
        7
    ),
    KotlinBug(
        "15.KT-32184",
        [pc.Lambdas(), pc.DataClasses(), pc.FunctionTypes(), pc.Nullables(),
         pc.SecondaryConstructor(), pc.Overloading()],
        True,
        sy.InternalCompilerError(),
        rc.WrongParams(),
        ct.Resolution(),
        12
    ),
    KotlinBug(
        "16.KT-10197",
        [pc.Overriding(), pc.Delegation(), pc.Inheritance()],
        False,
        sy.Runtime(sy.AbstractMethodError()),
        rc.MissingCase(),
        ct.MissingValiationChecks(),
        12
    ),
    KotlinBug(
        "17.KT-41693",
        [pc.Conditionals(),
         pc.Nullables(),
         pc.JavaInterop()],
        True,
        sy.Runtime(sy.NullPointerException()),
        rc.MissingCase(),
        ct.Approximation(),
        16
    ),
    KotlinBug(
        "18.KT-44420",
        [pc.Collections(),
         pc.VarTypeInference(),
         pc.TypeArgsInference(),
         pc.JavaInterop()],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Approximation(),
        9
    ),
    KotlinBug(
        "19.KT-35602",
        [pc.ParameterizedClasses(),
         pc.FBounded(),
         pc.Nullables(),
         pc.WildCardType(),
         pc.ParameterizedTypes(),
         pc.NullAssertion()],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Approximation(),
        6
    ),
    KotlinBug(
        "20.KT-6992",
        [pc.Overloading(),
         pc.ParameterizedClasses(),
         pc.SecondaryConstructor()],
        False,
        sy.MisleadingReport(),
        rc.InsufficientAlgorithmImplementation(),
        ct.Resolution(),
        3
    ),
]


kotlin_iter2 = [
    KotlinBug(
        "1.KT-31102",
        [pc.Lambdas(), pc.FunctionReferences(),
         pc.ParameterizedFunctions(), pc.FunctionTypes(),
         pc.TypeArgsInference(), pc.This()],
        True,
        sy.CompileTimeError(),
        rc.InsufficientAlgorithmImplementation(),
        ct.Inference(),
        8
    ),
    KotlinBug(
        "2.KT-3112",
        [pc.NestedClasses(),
         pc.ParameterizedClasses(),
         pc.TypeArgsInference()],
        False,
        sy.MisleadingReport(),
        rc.InsufficientAlgorithmImplementation(),
        ct.Inference(),
        4
    ),
    KotlinBug(
        "3.KT-11721",
        [pc.Overriding(), pc.Property()],
        False,
        sy.MisleadingReport(),
        rc.IncorrectSequence(),
        ct.Resolution(),
        3
    ),
    KotlinBug(
        "4.KT-39461",
        [pc.Coroutines(), pc.OperatorOverloading(),
         pc.Lambdas(),
         pc.TypeArgsInference(),
         pc.ParameterizedFunctions(),
         pc.FunctionTypes()
         ],
        True,
        sy.CompileTimeError(),
        rc.IncorrectComputation(),
        ct.Resolution(),
        11
    ),
    KotlinBug(
        "5.KT-15226",
        [pc.JavaInterop(),
         pc.Overriding(),
         pc.Inheritance(),
         pc.Delegation()],
        True,
        sy.Runtime(sy.WrongResult()),
        rc.DesignIssue(),
        ct.MissingValiationChecks(),
        15
    ),
    KotlinBug(
        "6.KT-6720",
        [pc.Overriding(),
         pc.JavaInterop(),
         pc.Inheritance()
         ],
        False,
        sy.Runtime(sy.AbstractMethodError()),
        rc.IncorrectComputation(),
        ct.Resolution(),
        8
    ),
    KotlinBug(
        "7.KT-37644",
        [pc.ElvisOperator(),
         pc.Collections(),
         pc.ParameterizedTypes()
         ],
        True,
        sy.InternalCompilerError(),
        rc.ExtraneousComputation(),
        ct.Inference(),
        3
    ),
    KotlinBug(
        "8.KT-22517",
        [pc.PropertyReference(),
         pc.OperatorOverloading(),
         pc.WildCardType(),
         pc.Subtyping(),
         pc.Delegation(),
         pc.ParameterizedTypes(),
         pc.Nullables(),
         pc.FlowTyping()],
        False,
        sy.Runtime(sy.NullPointerException()),
        rc.DesignIssue(),
        ct.Environment(),
        10
    ),
    KotlinBug(
        "9.KT-18522",
        [pc.Conditionals(), pc.Import(),
         pc.ParameterizedClasses(),
         pc.ReturnTypeInference(),
         pc.ParameterizedTypes()
         ],
        False,
        sy.InternalCompilerError(),
        rc.IncorrectCondition(),
        ct.TypeComparison(),
        9
    ),
    KotlinBug(
        "10.KT-8320",
        [pc.ParameterizedFunctions(),
         pc.BoundedPolymorphism(),
         pc.Subtyping(),
         pc.TryCatch()],
        False,
        sy.Runtime(sy.ClassCastException()),
        rc.MissingCase(),
        ct.MissingValiationChecks(),
        11
    ),
    KotlinBug(
        "11.KT-32081",
        [pc.ParameterizedClasses(),
         pc.ParameterizedFunctions(),
         pc.Singleton(),
         pc.TypeArgsInference(),
         pc.ParameterizedTypes(),
         pc.Inheritance(),
         pc.OperatorOverloading(),
         pc.Nothing(),
         pc.Subtyping(),
         pc.ExtensionFunctions()],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Inference(),
        5
    ),
    KotlinBug(
        "12.KT-11280",
        [pc.Overriding(),
         pc.Subtyping(),
         pc.FlowTyping()],
        False,
        sy.Runtime(sy.ClassCastException()),
        rc.DesignIssue(),
        ct.Inference(),
        13
    ),
    KotlinBug(
        "13.KT-3810",
        [pc.Inheritance(),
         pc.Overriding(),
         pc.Property(),
         ],
        False,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        ct.ErrorReporting(),
        6
    ),
    KotlinBug(
        "14.KT-17597",
        [pc.AccessModifiers(),
         pc.StaticMethod(),
         pc.Overloading(),
         pc.JavaInterop(),
         pc.FunctionReferences()],
        True,
        sy.CompileTimeError(),
        rc.IncorrectCondition(),
        ct.Resolution(),
        9
    ),
    KotlinBug(
        "15.KT-13597",
        [pc.AnonymousClass(), pc.Property(), pc.SecondaryConstructor()],
        False,
        sy.Runtime(sy.IllegalAccessError()),
        rc.InsufficientAlgorithmImplementation(),
        ct.MissingValiationChecks(),
        15
    ),
    KotlinBug(
        "16.KT-12738",
        [pc.ParameterizedFunctions(),
         pc.FunctionReferences()],
        True,
        sy.CompileTimeError(),
        rc.InsufficientAlgorithmImplementation(),
        ct.Resolution(),
        3
    ),
    KotlinBug(
        "17.KT-37627",
        [pc.Collections(),
         pc.Conditionals(),
         pc.ParamTypeInference(),
         pc.Nullables(),
         pc.Subtyping(),
         pc.TypeArgsInference(),
         pc.Lambdas(),
         pc.VarTypeInference()],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Inference(),
        5
    ),
    KotlinBug(
        "18.KT-12286",
        [pc.ParameterizedFunctions(),
         pc.TypeArgsInference(),
         pc.FunctionTypes(),
         pc.FBounded(),
         pc.Conditionals(),
         pc.FunctionReferences()],
        True,
        sy.CompileTimeError(),
        rc.InsufficientAlgorithmImplementation(),
        ct.Inference(),
        2
    ),
    KotlinBug(
        "19.KT-9630",
        [pc.ParameterizedClasses(),
         pc.MultipleImplements(),
         pc.ParameterizedFunctions(),
         pc.TypeArgsInference(),
         pc.VarTypeInference(),
         pc.ParameterizedTypes(),
         pc.FBounded(),
         pc.MultiBounds(),
         pc.ExtensionFunctions()],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Approximation(),
        8
    ),
    KotlinBug(
        "20.KT-25302",
        [pc.ParameterizedFunctions(),
         pc.TypeArgsInference(),
         pc.ParameterizedClasses(),
         pc.WildCardType(),
         pc.ParameterizedTypes(),
         ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Inference(),
        12
    )
]

kotlin_iter3 = [
    KotlinBug(
        "1.KT-31620",
        [pc.ParameterizedClasses(),
         pc.ParameterizedFunctions(),
         pc.Lambdas(),
         pc.VarTypeInference(),
         pc.BuilderInference(),
         pc.TypeArgsInference(),
         pc.ExtensionFunctions(),
         pc.FunctionTypes()],
        True,
        sy.CompileTimeError(),
        rc.WrongParams(),
        ct.Inference(),
        11
    ),
    KotlinBug(
        "2.KT-2277",
        [pc.Overloading(), pc.NestedClasses()],
        False,
        sy.Runtime(sy.AmbiguousMethodError()),
        rc.MissingCase(),
        ct.MissingValiationChecks(),
        5
    ),
    KotlinBug(
        "3.KT-9134",
        [pc.Nullables(), pc.Lambdas(), pc.FlowTyping()],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.IncorrectAnalysisMechanics(),
        6
    ),
    KotlinBug(
        "4.KT-35172",
        [pc.Nullables(), pc.ParameterizedFunctions(),
         pc.ExtensionFunctions(), pc.Lambdas(), pc.ElvisOperator(),
         pc.SafeNavigationOperator(), pc.TypeArgsInference()],
        True,
        sy.CompileTimeError(),
        rc.ExtraneousComputation(),
        ct.Inference(),
        5
    ),
    KotlinBug(
        "5.KT-41644",
        [
            pc.ParameterizedClasses(),
            pc.ParameterizedTypes(),
            pc.BoundedPolymorphism(),
            pc.Inheritance(),
            pc.FBounded(),
            pc.SealedClasses(),
            pc.NestedClasses(),
            pc.Cast()
        ],
        True,
        sy.CompilationPerformance(),
        rc.AlgorithmImproperlyImplemented(),
        ct.Inference(),
        41
    ),
    KotlinBug(
        "6.KT-30953",
        [
            pc.VarTypeInference(),
            pc.Conditionals(),
            pc.FunctionReferences(),
        ],
        False,
        sy.InternalCompilerError(),
        rc.WrongDataReference(),
        ct.ErrorReporting(),
        3
    ),
    KotlinBug(
        "7.KT-39470",
        [
            pc.Collections(),
            pc.ParameterizedTypes(),
            pc.FunctionReferences(),
            pc.Property(),
            pc.ExtensionFunctions(),
            pc.TypeArgsInference()
        ],
        True,
        sy.CompileTimeError(),
        rc.IncorrectCondition(),
        ct.Inference(),
        8
    ),
    KotlinBug(
        "8.KT-6999",
        [
            pc.SecondaryConstructor(),
            pc.TypeAnnotations()
        ],
        False,
        sy.Runtime(sy.VerifyError()),
        rc.IncorrectCondition(),
        ct.MissingValiationChecks(),
        8
    ),
    KotlinBug(
        "9.KT-13685",
        [
            pc.Collections(),
            pc.ParameterizedTypes(),
            pc.TypeArgsInference(),
            pc.Nullables(),
            pc.FunctionReferences()
        ],
        False,
        sy.InternalCompilerError(),
        rc.WrongDataReference(),
        ct.Resolution(),
        4
    ),
    KotlinBug(
        "10.KT-5511",
        [
           pc.ParameterizedClasses(),
           pc.NestedClasses(),
           pc.Inheritance(),
           pc.ParameterizedTypes(),
           pc.Enums()
        ],
        False,
        sy.MisleadingReport(),
        rc.WrongParams(),
        ct.ErrorReporting(),
        3
    ),
    KotlinBug(
        "11.KT-26816",
        [
            pc.TypeArgsInference(),
            pc.ParamTypeInference(),
            pc.Lambdas(),
            pc.Collections()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Inference(),
        9
    ),
    KotlinBug(
        "12.KT-33125",
        [
            pc.ParameterizedClasses(),
            pc.ParameterizedFunctions(),
            pc.ParameterizedTypes(),
            pc.TypeArgsInference(),
            pc.OperatorOverloading(),
            pc.Inheritance(),
            pc.BuilderInference(),
            pc.Collections(),
            pc.FunctionTypes(),
            pc.Lambdas(),
            pc.ExtensionFunctions(),
            pc.UseVariance(),
            pc.AugmentedAssignmentOperator(),
        ],
        True,
        sy.InternalCompilerError(),
        rc.InsufficientAlgorithmImplementation(),
        ct.IncorrectAnalysisMechanics(),
        12
    ),
    KotlinBug(
        "13.KT-7383",
        [
            pc.FunctionAPI(),
            pc.WildCardType(),
            pc.Subtyping(),
            pc.ParameterizedTypes(),
            pc.ParamTypeInference(),
            pc.Lambdas()
        ],
        False,
        sy.InternalCompilerError(),
        rc.ExtraneousComputation(),
        ct.ErrorReporting(),
        3
    ),
    KotlinBug(
        "14.KT-33542",
        [
            pc.Coroutines(),
            pc.ParameterizedClasses(),
            pc.DeclVariance(),
            pc.BoundedPolymorphism(),
            pc.ParameterizedTypes(),
            pc.BuilderInference(),
            pc.Overriding(),
            pc.Inheritance(),
            pc.FunctionTypes(),
            pc.ExtensionFunctions(),
            pc.Lambdas()
        ],
        False,
        sy.InternalCompilerError(),
        rc.WrongParams(),
        ct.Environment(),
        22
    ),
    KotlinBug(
        "15.KT-15391",
        [
            pc.Coroutines(),
            pc.NamedArgs(),
            pc.Inheritance(),
            pc.FunctionTypes(),
            pc.AnonymousClass(),
            pc.ParameterizedTypes(),
            pc.Overriding()
        ],
        False,
        sy.Runtime(sy.AbstractMethodError()),
        rc.MissingCase(),
        ct.MissingValiationChecks(),
        15
    ),
    KotlinBug(
        "16.KT-9320",
        [
            pc.TypeAnnotations(),
            pc.AnonymousClass()
        ],
        True,
        sy.Runtime(sy.WrongResult()),
        rc.MissingCase(),
        ct.Resolution(),
        5
    ),
    KotlinBug(
        "17.KT-13926",
        [
            pc.TypeAnnotations(),
        ],
        False,
        sy.MisleadingReport(),
        rc.MissingCase(),
        ct.Environment(),
        6
    ),
    KotlinBug(
        "18.KT-9816",
        [
            pc.ParameterizedClasses(),
            pc.Inheritance(),
            pc.TryCatch(),
            pc.ParameterizedTypes()
        ],
        False,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        ct.MissingValiationChecks(),
        10
    ),
    KotlinBug(
        "19.KT-4462",
        [
            pc.OperatorOverloading(),
        ],
        False,
        sy.InternalCompilerError(),
        rc.IncorrectComputation(),
        ct.Transformation(),
        14
    ),
    KotlinBug(
        "20.KT-11203",
        [
            pc.OperatorOverloading(),
            pc.ExtensionFunctions()
        ],
        False,
        sy.Runtime(sy.VerifyError()),
        rc.IncorrectCondition(),
        ct.Resolution(),
        8
    )
]

kotlin_iter4 = [
    KotlinBug(
        "1.KT-2418",
        [
            pc.Enums()
        ],
        False,
        sy.Runtime(sy.WrongResult()),
        rc.MissingCase(),
        ct.MissingValiationChecks(),
        3
    ),
    KotlinBug(
        "2.KT-12982",
        [
            pc.AccessModifiers(),
            pc.ParameterizedTypes(),
            pc.Reflection(),
            pc.FunctionReferences(),
            pc.VarTypeInference()
        ],
        True,
        sy.CompileTimeError(),
        rc.WrongParams(),
        ct.Inference(),
        12
    ),
    KotlinBug(
        "3.KT-41470",
        [
            pc.Coroutines(),
            pc.ParameterizedClasses(),
            pc.ParameterizedTypes(),
            pc.TypeArgsInference(),
            pc.DeclVariance(),
            pc.AnonymousClass(),
            pc.ExtensionFunctions(),
            pc.ParameterizedFunctions(),
            pc.Inheritance(),
            pc.Overriding(),
            pc.Lambdas(),
            pc.FunctionTypes(),
            pc.BuilderInference()
        ],
        True,
        sy.Runtime(sy.NullPointerException()),
        rc.MissingCase(),
        ct.Inference(),
        29
    ),
    KotlinBug(
        "4.KT-12477",
        [
        ],
        False,
        sy.MisleadingReport(),
        rc.MissingCase(),
        ct.ErrorReporting(),
        1
    ),
    KotlinBug(
        "5.KT-44153",
        [
        ],
        False,
        sy.CompilationPerformance(),
        rc.IncorrectCondition(),
        ct.Transformation(),
        1
    ),
    KotlinBug(
        "6.KT-8484",
        [
            pc.Enums(), pc.SecondaryConstructor()
        ],
        True,
        sy.CompileTimeError(),
        rc.IncorrectCondition(),
        ct.MissingValiationChecks(),
        4
    ),
    KotlinBug(
        "7.KT-16232",
        [
            pc.NestedClasses(),
            pc.Singleton()
        ],
        False,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        ct.MissingValiationChecks(),
        13
    ),
    KotlinBug(
        "8.KT-17611",
        [
            pc.AnonymousClass()
        ],
        True,
        sy.MisleadingReport(),
        rc.DesignIssue(),
        ct.MissingValiationChecks(),
        5
    ),
    KotlinBug(
        "9.KT-37554",
        [
            pc.ParameterizedClasses(),
            pc.DeclVariance(),
            pc.BoundedPolymorphism(),
            pc.Nullables(),
            pc.FBounded(),
            pc.Inheritance(),
            pc.ParameterizedFunctions(),
            pc.ParameterizedTypes(),
            pc.TypeArgsInference(),
            pc.ElvisOperator()
        ],
        True,
        sy.CompileTimeError(),
        rc.IncorrectComputation(),
        ct.Inference(),
        13
    ),
    KotlinBug(
        "10.KT-23854",
        [
            pc.ParameterizedClasses(),
            pc.ParameterizedFunctions(),
            pc.TypeArgsInference(),
            pc.UseVariance(),
            pc.ParameterizedTypes()
        ],
        True,
        sy.CompileTimeError(),
        rc.DesignIssue(),
        ct.Inference(),
        11
    ),
    KotlinBug(
        "11.KT-6399",
        [
            pc.JavaInterop(),
            pc.Conditionals(),
            pc.Enums()
        ],
        True,
        sy.Runtime(),
        rc.DesignIssue(),
        ct.MissingValiationChecks(),
        11
    ),
    KotlinBug(
        "12.KT-30826",
        [
            pc.MultipleImplements(),
            pc.Nullables(),
            pc.VarTypeInference(),
            pc.Cast(),
            pc.Lambdas(),
            pc.FlowTyping()
        ],
        False,
        sy.Runtime(sy.NullPointerException()),
        rc.MissingCase(),
        ct.Approximation(),
        18
    ),
    KotlinBug(
        "13.KT-11490",
        [
            pc.ParameterizedClasses(),
            pc.DeclVariance(),
            pc.Inheritance(),
            pc.ParameterizedTypes(),
            pc.ParameterizedFunctions(),
            pc.TypeArgsInference()
        ],
        False,
        sy.InternalCompilerError(),
        rc.IncorrectCondition(),
        ct.MissingValiationChecks(),
        7
    ),
    KotlinBug(
        "14.KT-37579",
        [
            pc.ParameterizedClasses(),
            pc.ParameterizedTypes(),
            pc.OperatorOverloading(),
            pc.FunctionTypes(),
            pc.Nullables(),
            pc.Lambdas(),
            pc.TypeArgsInference(),
            pc.SafeNavigationOperator(),
            pc.ExtensionFunctions()
        ],
        True,
        sy.CompileTimeError(),
        rc.IncorrectCondition(),
        ct.Resolution(),
        10
    ),
    KotlinBug(
        "15.KT-32462",
        [
            pc.Conditionals(),
            pc.FunctionReferences(),
            pc.Subtyping(),
            pc.TryCatch(),
        ],
        True,
        sy.InternalCompilerError(),
        rc.IncorrectComputation(),
        ct.Resolution(),
        8
    ),
    KotlinBug(
        "16.KT-32235",
        [
            pc.ParameterizedClasses(),
            pc.Collections(),
            pc.ParameterizedTypes(),
            pc.WildCardType(),
            pc.Nullables(),
            pc.FlowTyping(),
            pc.Property(),
            pc.ParamTypeInference()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Approximation(),
        17
    ),
    KotlinBug(
        "17.KT-10896",
        [
            pc.ParameterizedClasses(),
            pc.FlowTyping(),
            pc.ParameterizedFunctions(),
            pc.ParameterizedTypes(),
            pc.Subtyping(),
            pc.Inheritance(),
            pc.FunctionTypes(),
            pc.Overriding(),
            pc.Conditionals(),
            pc.Lambdas()
        ],
        False,
        sy.Runtime(sy.ClassCastException()),
        rc.MissingCase(),
        ct.Resolution(),
        35
    ),
    KotlinBug(
        "18.KT-31025",
        [
            pc.JavaInterop(),
            pc.ParameterizedClasses(),
            pc.ParameterizedFunctions(),
            pc.FunctionTypes(),
            pc.TypeArgsInference(),
            pc.UseVariance(),
            pc.FunctionReferences(),
            pc.SAM(),
            pc.FunctionAPI()
        ],
        True,
        sy.CompileTimeError(),
        rc.IncorrectCondition(),
        ct.Resolution(),
        12
    ),
    KotlinBug(
        "19.KT-42791",
        [
            pc.ParameterizedTypes(),
            pc.ParameterizedClasses(),
            pc.BoundedPolymorphism(),
            pc.ParameterizedFunctions(),
            pc.Inheritance(),
            pc.TypeArgsInference(),
            pc.NestedClasses()
        ],
        True,
        sy.CompilationPerformance(),
        rc.DesignIssue(),
        ct.Inference(),
        14
    ),
    KotlinBug(
        "20.KT-13181",
        [
            pc.Import(),
            pc.Typedefs(),
            pc.Lambdas(),
            pc.FunctionTypes(),
            pc.DeclVariance(),
            pc.ParameterizedClasses(),
            pc.ParameterizedTypes(),
            pc.ExtensionFunctions(),
            pc.TypeArgsInference()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Resolution(),
        0
    ),
]
