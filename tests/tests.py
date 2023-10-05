import pytest
from pathlib import Path

from pmgr.project import Project,TaskException

@pytest.fixture(scope="function")
def testproj():
    tproj = Project('mytestproj')
    yield tproj
    tproj.delete()

def test_add(testproj):
    testproj.add_task('dosomething')
    assert 'dosomething' in testproj.get_tasks()

def test_add_duplicate(testproj):
    testproj.add_task('dosomething')
    with pytest.raises(TaskException):
        testproj.add_task('dosomething')

def test_remove_task(testproj):
    testproj.add_task('something')
    testproj.remove_task('something')
    assert 'something' not in testproj.get_tasks()

def test_remove_inexistent_task(testproj):
    with pytest.raises(TaskException):
        testproj.remove_task('something')
    return 

def test_write_after_remove(testproj):
    testproj.add_task('something')
    testproj.add_task('somethingelse')
    testproj.remove_task('somethingelse')
    assert True
