# table.py

import sys

#def print_table(objects, colnames):
#    '''
#    Make a nicely formatted table showing attributes from a list of objects
#    :param objects:
#    :param colnames:
#    :return:
#    '''
#
#    # Emit table header
#    for colname in colnames:
#        print('{:>10s}'.format(colname), end=' ')
#    print()
#    for obj in objects:
#        # Emmit a row of table data
#        for colname in colnames:
#           print('{:>10s}'.format(str(getattr(obj, colname))), end=' ')
#        print()

#def print_table(objects, colnames, formatter):
#    '''
#    Make a nicely formatted table showing attributes from a list of objects
#    :param objects:
#    :param colnames:
#    :return:
#    '''
#
#    # Emit table header
#    formatter.headings(colnames)
#    for obj in objects:
#        # Emmit a row of table data
#        rowdata = [str(getattr(obj, colname)) for colname in colnames]
#        formatter.row(rowdata)

class TableFormatter(object):
    # Serves a design spec for making tables (user inheritance to customize)
    def __init__(self, outfile=None):
        if outfile == None:
            outfile = sys.stdout
        self.outfile = outfile

    def print_table(self, objects, colnames):
        '''
        Make a nicely formatted table showing attributes from a list of objects
        :param objects:
        :param colnames:
        :return:
        '''

        # Emit table header
        self.headings(colnames)
        for obj in objects:
            # Emmit a row of table data
            rowdata = [str(getattr(obj, colname)) for colname in colnames]
            self.row(rowdata)

    def headings(self, headers):
        raise NotImplementedError

    def row(self, rowdata):
        raise NotImplementedError

class TextTableFormatter(TableFormatter):
    def __init__(self, outfile=None, width=10):
        super().__init__( outfile) # Initialize parent
        self.width = width
    def headings(self, headers):
        for header in headers:
            print('{:>{}s}'.format(header, self.width), end=' ', file=self.outfile)
        print(file=self.outfile)

    def row(self, rowdata)\
            :
        for item in rowdata:
            print('{:>{}s}'.format(item, self.width), end=' ', file=self.outfile)
        print(file=self.outfile)

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print('<th>{}</th>'.format(h), end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print('<td>{}</td>'.format(d), end='')
        print('</tr>')

class QuotedMixin(object):
    def row(self, rowdata):
        quoted = ['"{}"'.format(d) for d in rowdata]
        super().row(quoted)
