#!/usr/bin/env python
# encoding: utf-8
"""
vesper-export.py

Created by Brian Partridge.
Copyright (c) 2013 Brian Partridge. All rights reserved.
"""

import sys
from optparse import OptionParser
import os
import sqlite3

def exportNotes(cursor, destDir, markdownify=False):
    print "Exporting to '%s':" % destDir
    query = "SELECT uniqueId,text,archived,attachmentUniqueID,tags from notes;"
    for record in cursor.execute(query):
        id = record[0]
        text = record[1].encode("utf-8") if record[1] else None
        archived = bool(record[2])
        imageId = record[3].encode("utf-8") if record[3] else None
        tags = record[4].encode("utf-8") if record[4] else None

        ext = ".md" if markdownify else ".txt"
        title = text.splitlines()[0].strip() + ext
        path = os.path.join(destDir,title)
        file = open(path, "w")
        
        if imageId:
            if markdownify:
                file.write("![Header Image](images/%s)\n\n" % imageId)
            else:
                file.write("Image: images/%s\n\n", imageId)
        if markdownify:
            file.write("# ")
        file.write(text)
        if tags:
            file.write("\nTags: %s" % tags)
        file.close()
        print "  Exported '%s'" % title
    print "Done"
    pass

def main2(options, args):
    source_file = options.file
    dest_dir = os.path.expanduser(options.out)
    verbose = options.verbose
    markdownify = options.markdown
    
    if not source_file:
        print "A source database file is required."
        sys.exit(1)
    if not dest_dir or not os.path.isdir(dest_dir):
        print "An output directory is required."
        sys.exit(1)
        
    db = sqlite3.connect(source_file)
    cursor = db.cursor()
    exportNotes(cursor, dest_dir, markdownify)
    db.close()
    pass

def main():
    parser = OptionParser(version="%prog 1.0")
    parser.add_option("-f", "--file", 
                      dest="file",
                      help="read from FILE", 
                      metavar="FILE")
    parser.add_option("-o", "--out", 
                      dest="out",
                      help="save output to DIR", 
                      metavar="DIR")
    parser.add_option("-m", "--markdown", 
                      action="store_true",
                      dest="markdown",
                      default=False,
                      help="format exported notes in with markdown markup")
    parser.add_option("-v", "--verbose",
                      action="store_true", 
                      dest="verbose", 
                      default=False,
                      help="display additional information")

    (options, args) = parser.parse_args()
    main2(options, args)

if __name__ == "__main__":
	sys.exit(main())
