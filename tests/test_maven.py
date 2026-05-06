from playground.maven import match_paths


def test_match_paths_includes_matching_paths() -> None:
    paths = [
        "src/main/java/App.java",
        "src/main/resources/config.yml",
        "README.md",
    ]

    assert match_paths(paths, ["src/main/java/*.java"]) == [
        "src/main/java/App.java",
    ]


def test_match_paths_excludes_after_inclusion() -> None:
    paths = [
        "src/main/java/App.java",
        "src/test/java/AppTest.java",
        "src/main/java/Service.java",
    ]

    assert match_paths(paths, ["src/**/*.java"], ["src/test/**"]) == [
        "src/main/java/App.java",
        "src/main/java/Service.java",
    ]


def test_match_paths_accepts_multiple_include_patterns() -> None:
    paths = [
        "pom.xml",
        "src/main/java/App.java",
        "src/main/resources/application.properties",
        "docs/usage.md",
    ]

    assert match_paths(paths, ["pom.xml", "src/main/resources/*"]) == [
        "pom.xml",
        "src/main/resources/application.properties",
    ]


def test_match_paths_returns_empty_list_for_empty_include() -> None:
    assert match_paths(["pom.xml"], []) == []


def test_match_paths_preserves_input_order() -> None:
    paths = [
        "src/main/java/Third.java",
        "src/main/java/First.java",
        "src/main/java/Second.java",
    ]

    assert match_paths(paths, ["src/main/java/*.java"]) == paths


def test_match_paths_returns_empty_list_when_no_paths_match() -> None:
    assert match_paths(["README.md", "docs/usage.md"], ["src/**/*.java"]) == []


def test_match_paths_does_not_mutate_inputs() -> None:
    paths = [
        "pom.xml",
        "src/main/java/App.java",
        "src/test/java/AppTest.java",
    ]
    include = ["pom.xml", "src/**/*.java"]
    exclude = ["src/test/**"]
    original_paths = list(paths)
    original_include = list(include)
    original_exclude = list(exclude)

    assert match_paths(paths, include, exclude) == [
        "pom.xml",
        "src/main/java/App.java",
    ]
    assert paths == original_paths
    assert include == original_include
    assert exclude == original_exclude
