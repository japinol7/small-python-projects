import logging

from lxml import etree
import xmltodict

log = logging.getLogger(__name__)


def add_child_to_xml_obj(parent, child_name, attrib=None, text=None):
    """Adds a child element to a xml element object."""
    child = etree.SubElement(parent, child_name, attrib=attrib)
    child.text = str(text) if text else ''
    return child


def parse_listdict2xml(input_vals, root_name: str, element_name: str, elements_with_attribs: dict = None):
    """Parses a list of dictionaries and returns a xml object.
    The root_name is the name of the root element you want to get.
    The element_name is the name of the elements you want to add to the root.
    You can pass a dictionary with attributes for each element to be added
    as an attribute to the element.
    Example of usage:
        from datetime import datetime
        elements_with_attribs = {
            'id': {'date': datetime.now().strftime('%Y-%m-%d')},
        }
        input_vals = [
            {'id': 2, 'name': 'Shinji Ikari'},
            {'id': 3, 'name': 'Rei Ayanami'},
        ]
        root = parse_listdict2xml(input_vals, 'npcs', 'npc', elements_with_attribs)
        print(pformat_xml(root))
    Example of output:
        <npcs>
            <npc>
                <id date="2024-05-11">2</id>
                <name>Shinji Ikari</name>
            </npc>
            <npc>
                <id date="2024-05-11">3</id>
                <name>Rei Ayanami</name>
            </npc>
        </npcs>
    """
    if elements_with_attribs is None:
        elements_with_attribs = {}

    root = etree.Element(root_name)
    for anime in input_vals:
        anime_ = etree.SubElement(root, element_name)
        for k, v in anime.items():
            add_child_to_xml_obj(anime_, k, attrib=elements_with_attribs.get(k), text=str(v))
    return root


def parse_xml2dict(xml_input) -> dict:
    """Parses a xml str or buffer and returns a dictionary."""
    try:
        return xmltodict.parse(xml_input, process_namespaces=False)
    except Exception as e:
        log.info("Error parsing xml to dict: %s", e)


def parse_xml_obj_to_dict_filtered_by_tag(root, tag_to_find) -> dict:
    """Parses a xml etree object, filters it by a tag and returns a dictionary."""
    children = root.findall(tag_to_find)

    def get_tags(children_):
        out = {}
        for child in list(children_):
            if len(list(child)):
                if child.tag not in out:
                    out[child.tag] = []
                out[child.tag].append(get_tags(child))
            else:
                out[child.tag] = child.text
                if child.attrib:
                    out[f"{child.tag}_attrib"] = {k: v for k, v in child.attrib.items()}
        return out
    return get_tags(children)


def pformat_xml(element, encoding='utf-8', **kwargs) -> str:
    """Pretty format xml object to string."""
    xml_ = etree.tostring(element, pretty_print=True, **kwargs)
    return xml_.decode(encoding)
