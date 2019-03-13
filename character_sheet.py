"""Create an PDF character sheet from a Character object.

To use this you first need to install the pypdf2 package::

    pip install pypdf2

You also need a PDF template (included). This script assumes that the PDF has
certain fields to be filled in, so if the template changes then the script may
break.

The included template was brazenly stolen from reddit::

    https://www.reddit.com/r/dndnext/comments/7muor6/the_official_dd_5e_character_sheet_as_an_editable/

To create a new character sheeet, do this::

    python character_sheet.py TWC-DnD-5E-Character_sheet-v1.6.pdf my-character.pdf

To list the fields in the input template (useful for development)::

    python character_sheet.py --fields TWC-DnD-5E-Character_sheet-v1.6.pdf

Future work ideas:

- It would probably be better to separate character sheet generation from
  character generation. The character creation phase could export the character
  to JSON or something, and sheet generation could read that JSON.

- Fix the template so that the field names don't have spurious spaces. Or just
  create out own template. In fact, the "template" could be entirely in Python
  with no need for an external PDF, but this might be more trouble than it's
  worth.

"""

import sys

import PyPDF2

from Generator import make_character


def update_fields(pdf, fields):
    for page_number in range(pdf.getNumPages()):
        page = pdf.getPage(page_number)
        pdf.updatePageFormFieldValues(page, fields)


def show_fields(filename):
    with open(filename, mode='rb') as handle:
        pdf = PyPDF2.PdfFileReader(handle)
        fields = pdf.getFormTextFields()
        for field in sorted(fields):
            print("'{}'".format(field))


def character_to_fields(character, fields):
    """Fill in form fields with values from a Character.
    """
    fields['CharacterName'] = character.name
    # This looks like a bug in the template. There's a space following "Race" in the the field name.
    # There are certainly more fields like this, so beware!
    fields['Race '] = character.race_name
    fields['STR'] = character.stats.strength
    fields['DEX'] = character.stats.dexterity

    # TODO: Fill in `fields` with the rest of the character information.

    return fields


def main(args):
    # Helpful development tool. This will print the fields in the source PDF.
    if args[1] == '--fields':
        show_fields(args[2])
        return

    # Make a character and save it to PDF
    character = make_character()

    template = args[1]
    output_file = args[2]

    with open(template, mode='rb') as source_handle:
        source = PyPDF2.PdfFileReader(source_handle)
        fields = source.getFormTextFields()
        dest = PyPDF2.PdfFileWriter()
        dest.cloneDocumentFromReader(source)

        fields = character_to_fields(character, fields)
        update_fields(dest, fields)

        with open(output_file, mode='wb') as dest_handle:
            dest.write(dest_handle)


if __name__ == '__main__':
    main(sys.argv)
