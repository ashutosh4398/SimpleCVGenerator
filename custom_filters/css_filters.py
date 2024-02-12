 
from django import template 
  
register = template.Library() 

@register.filter
def add_attrs(field, attr):
    # attr format -> class:mb-2 spr-2;id:example
    input_attrs = [x.strip() for x in attr.split(";")]
    elem_attrs = {}
    for attribute in input_attrs:
        name, props = attribute.split(":")
        elem_attrs[name.strip()] = props.strip()
    return field.as_widget(attrs=elem_attrs)