# Vesper Export

## Description
A script to export your notes from the [Vesper](http://vesperapp.co) iOS app to text files.
Exported notes can include markdown formatting with the `--markdown` switch.

## Known Issues

- This was developed against Vesper 1.003. The data model has changed in newer versions and the script is incompatible with version 2+.  
- Supporting new Vesper data model versions is a moving target.  The syncing feature added in 2.0 removes the need for exporting for backup.  That said, patches are welcome.

## Usage

- Using a tool like [PhoneView](https://www.ecamm.com/mac/phoneview/):
  - Extract the `Vesper-Notes.sqlite3`
  - Extract the `Attachments` directory
- Create an output directory
- Move the exported `Attachements` directory into the output directory and rename it to 'images'.
- Run `vesper-export.py`

        python vesper-export.py -f <path to Vesper-Notes.sqlite3> -o <path to output directory> [--markdown]

- Done

## License
[MIT](LICENSE.txt)

## Contact
[Brian Partridge](http://brianpartridge.name) - @brianpartridge on [Twitter](http://twitter.com/brianpartridge) and [App.Net](http://alpha.app.net/brianpartridge)
