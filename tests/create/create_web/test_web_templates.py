import pytest
import os
from io import StringIO
from pathlib import Path
from distutils.dir_util import copy_tree

from cookietemple.create.create import choose_domain
from cookietemple.util.dir_util import delete_dir_tree
from tests.create.create_cli.test_cli_template_creation import (subdir_dependabot, subdir_github)


@pytest.fixture
def valid_domains():
    return ['cli', 'gui', 'web']


def docs_subdir(path) -> set:
    return {Path(f'{path}/docs/conf.py'), Path(f'{path}/docs/Makefile'), Path(f'{path}/docs/contributing.rst'),
            Path(f'{path}/docs/authors.rst'),
            Path(f'{path}/docs/installation.rst'), Path(f'{path}/docs/make.bat'), Path(f'{path}/docs/index.rst'),
            Path(f'{path}/docs/usage.rst'),
            Path(f'{path}/docs/changelog.rst'), Path(f'{path}/docs/readme.rst')}


def deployment_script_tests(path) -> set:
    return {Path(f'{path}/deployment_scripts/projectname'), Path(f'{path}/deployment_scripts/projectname.service'),
            Path(f'{path}/deployment_scripts/README.md'),
            Path(f'{path}/deployment_scripts/setup.sh')}


def website_front_end_tests(path) -> set:
    return {Path(f'{path}/projectname/handlers'), Path(f'{path}/projectname/static'),
            Path(f'{path}/projectname/templates'),
            Path(f'{path}/projectname/translations'), Path(f'{path}/projectname/app.py'),
            Path(f'{path}/projectname/config.py'),
            Path(f'{path}/projectname/__init__.py'), Path(f'{path}/projectname/server.py')}


def subdir_tests(path) -> set:
    return {Path(f'{path}/tests/__init__.py'), Path(f'{path}/tests/projectname.py')}


def posix_path_super_dir(path) -> set:
    return {Path(f'{path}/MANIFEST.in'), Path(f'{path}/.editorconfig'), Path(f'{path}/Makefile'),
            Path(f'{path}/README.rst'),
            Path(f'{path}/tests'), Path(f'{path}/readthedocs.yml'), Path(f'{path}/babel.cfg'),
            Path(f'{path}/requirements_dev.txt'),
            Path(f'{path}/.travis.yml'), Path(f'{path}/.gitignore'), Path(f'{path}/projectname'),
            Path(f'{path}/.github'),
            Path(f'{path}/setup.py'), Path(f'{path}/.cookietemple.yml'), Path(f'{path}/CODE_OF_CONDUCT.rst'),
            Path(f'{path}/docs'),
            Path(f'{path}/deployment_scripts'), Path(f'{path}/requirements.txt'), Path(f'{path}/setup.cfg'),
            Path(f'{path}/CHANGELOG.rst'),
            Path(f'{path}/CONTRIBUTING.rst'), Path(f'{path}/LICENSE'), Path(f'{path}/AUTHORS.rst'),
            Path(f'{path}/.dependabot'),
            Path(f'{path}/tox.ini'), Path(f'{path}/cookietemple.cfg')}


# TODO: USE LINTING (LIKE NF CORE TOOLS) TO TEST COOKIECUTTER WITH EXTRA_CONTENT
@pytest.mark.skip(reason='MAJOR REFACTORING HAPPENING')
def test_choose_domain_web_basic_website_flask(monkeypatch, valid_domains, tmp_path) -> None:
    """
    This test tests the creation of a whole python flask website template without GitHub Repo creation!
    """
    prompt = StringIO(f'{valid_domains[2]}\npython\nname\nmail\nprojectname\ndesc\n0.1.0'
                      f'\nMIT\nmyGitHubName\npypiname\nClick\npytest\nwebsite\nflask\nbasic\ndmydomain.com\nvmname\nn')
    monkeypatch.setattr('sys.stdin', prompt)
    choose_domain('')
    copy_tree(f'{Path.cwd()}/projectname', str(tmp_path))
    delete_dir_tree(Path(f'{Path.cwd()}/projectname'))
    assert (set(tmp_path.iterdir()) == posix_path_super_dir(tmp_path) and set(Path(tmp_path / 'docs').iterdir())
            == docs_subdir(tmp_path) and set(Path(tmp_path / 'tests').iterdir()) == subdir_tests(tmp_path) and
            set(Path(tmp_path / '.dependabot').iterdir()) == subdir_dependabot(tmp_path) and
            set(Path(tmp_path / '.github').iterdir()) == subdir_github(tmp_path) and
            set(Path(tmp_path / 'projectname').iterdir()) == website_front_end_tests(tmp_path) and
            set(Path(tmp_path / 'deployment_scripts').iterdir()) == deployment_script_tests(tmp_path))


# TODO: USE LINTING (LIKE NF CORE TOOLS) TO TEST COOKIECUTTER WITH EXTRA_CONTENT
@pytest.mark.skip(reason='MAJOR REFACTORING HAPPENING')
def test_choose_domain_web_advanced_website_flask(monkeypatch, valid_domains, tmp_path) -> None:
    """
    This test tests the creation of a whole python flask website template without GitHub Repo creation!
    """
    prompt = StringIO(f'{valid_domains[2]}\npython\nname\nmail\nprojectname\ndesc\n0.1.0'
                      f'\nMIT\nmyGitHubName\npypiname\nClick\npytest\nwebsite\nflask\nadvanced\ndmydomain.com\nvmname\nn')
    monkeypatch.setattr('sys.stdin', prompt)
    choose_domain('')
    copy_tree(f'{Path.cwd()}/projectname', str(tmp_path))
    delete_dir_tree(Path(f'{Path.cwd()}/projectname'))
    assert (set(tmp_path.iterdir()) == posix_path_super_dir(tmp_path) and set(Path(tmp_path / 'docs').iterdir())
            == docs_subdir(tmp_path) and set(Path(tmp_path / 'tests').iterdir()) == subdir_tests(tmp_path) and
            set(Path(tmp_path / '.dependabot').iterdir()) == subdir_dependabot(tmp_path) and
            set(Path(tmp_path / '.github').iterdir()) == subdir_github(tmp_path) and
            set(Path(tmp_path / 'projectname').iterdir()) == website_front_end_tests(tmp_path) and
            set(Path(tmp_path / 'deployment_scripts').iterdir()) == deployment_script_tests(tmp_path))
