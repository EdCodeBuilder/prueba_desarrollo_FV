# Excel Transformer

This Odoo module allows you to transform Excel files according to user-defined transformation rules. The module uses the Python Pandas library to read and write Excel files, and allows you to define transformation rules for each column of the file. Transformation rules can be either numeric or alphanumeric, and specify the size of each transformed field. The module also removes the comma from the generated CSV file and adds the Content-Disposition header to the output file.

[![Odoo][Odoo]][Odoo-url]

## Features

- Transforms Excel files according to user-defined transformation rules.
- Uses the Python Pandas library to read and write Excel files.
- Allows you to define transformation rules for each column of the file.
- Transformation rules can be either numeric or alphanumeric, and specify the size of each transformed field.
- Removes the comma from the generated CSV file.

## Requirements

[![Python][Python]][Python-url]

- Odoo 16 or higher.
- Python Pandas library.

## Installation

1. Download the module from this repository.
2. Copy the module to the addons folder of your Odoo instance.
3. Update the list of installed modules in the Odoo web interface.
4. Find the module in the list of available modules and install it.

## Usage

1. Upload an Excel file to the "Excel File" field in the module form.
2. Define transformation rules for each column of the file in the Python code of the `ExcelTransformer` model.
3. Click the "Process Excel File" button to transform the Excel file according to the defined rules.
4. Download the transformed file by clicking the "Transformed File" link.

## For `excel_transformer_desktop`

1. install `requirements.txt`

```sh
python -m pip install -r requirements.txt
```

2. Execute `medio.py`

```sh
python .\medio.py
```

## Credits

This module was developed by [EdCodeBuilder](https://github.com/EdCodeBuilder).

## Contribution

If you want to contribute to this module, please send a pull request or contact the author.

## License

This module is available under the _GNU General Public License v3.0_. See the LICENSE file for more information.

## Contact

- Eduardo A. Peña - @Eduardo_A_PR - edurado.andres@gmail.com
- Project Link: [https://github.com/EdCodeBuilder/prueba_desarrollo_FV](https://github.com/EdCodeBuilder/prueba_desarrollo_FV)
- [LinkedIn](https://www.linkedin.com/in/eduardoandrespe%C3%B1arojas/)

[Odoo-url]: https://odoo.com/
[Odoo]: https://miro.medium.com/v2/resize:fit:1400/format:webp/1*nruLj59qN3aZJnb9aDTJ5g.png
[Python-url]: https://www.python.org/
[Python]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
