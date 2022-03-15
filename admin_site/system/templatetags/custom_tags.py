from django import template
import os

register = template.Library()


@register.filter
def add_class(field, class_name):
    """Add CSS classes to tags, e.g. django generated forms."""
    return field.as_widget(attrs={"class": " ".join((field.css_classes(), class_name))})


@register.simple_tag
def set_css_class_active(url_name, match):
    """
    Set css class active depending on url_name and match.

    url_name is the 'name' of an entry in urls.py
    match is a string to be matched in url_name
    """
    if match in url_name:
        # Don't highlight Scripts when on Security Scripts page.
        if match == "script" and "security_script" in url_name:
            return
        return "active"


# Useful for debugging
@register.filter
def get_fields(obj):
    return [(field.name, field.value_to_string(obj)) for field in obj._meta.fields]


@register.filter
def file_basename(value):
    return os.path.basename(value.file.name)
