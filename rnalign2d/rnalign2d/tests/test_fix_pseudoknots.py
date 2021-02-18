import pytest

from rnalign2d.fix_pseudoknots import \
    structure_to_representation, representation_to_structure


@pytest.mark.parametrize("in_content, out_content", [
    ('(((...)))', '(((...)))'),
    ('(((...[[[...)))...]]]', '(((...[[[...)))...]]]'),
    ('[[[...(((...]]]...)))', '(((...[[[...)))...]]]'),
    ('[[[...(((...{{{...]]]...)))...}}}', '(((...[[[...{{{...)))...]]]...}}}'),
    ('(((.[[[.{{{.))).(((.<<.]]]..(((.}}}.))).)))>>',
     '(((.[[[.{{{.))).(((.<<.]]]..(((.}}}.))).)))>>'),
    ('(((.[[[.{{{.))).(((.<<.]]].>>.(((.}}}.))).)))',
     '(((.[[[.{{{.))).(((.((.]]].)).(((.}}}.))).)))'),
    ('(((.[[[.{{{.))).(((.<<.]]]..(((.[[[.}}}.))).)))]]]>>',
     '(((.[[[.{{{.))).(((.<<.]]]..(((.[[[.}}}.))).)))]]]>>'),
    ('(((.[[[.{{{.))).(((.<<.]]]..(((.AAA.}}}.))).)))aaa>>',
     '(((.[[[.{{{.))).(((.<<.]]]..(((.[[[.}}}.))).)))]]]>>'),
    ('[[[.(((.{{{.]]].[[[.<<.)))..[[[.(((.}}}.]]].]]])))>>',
     '(((.[[[.{{{.))).(((.<<.]]]..(((.[[[.}}}.))).)))]]]>>'),
])
def test_fix_pseudoknots(in_content, out_content):
    result = representation_to_structure(
                in_content, structure_to_representation(in_content))
    assert result == out_content
