# table.py

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

def print_table(objects, colnames, formatter):
    '''
    Make a nicely formatted table showing attributes from a list of objects
    :param objects:
    :param colnames:
    :return:
    '''

    # Emit table header
    formatter.headings(colnames)
    for obj in objects:
        # Emmit a row of table data
        rowdata = [str(getattr(obj, colname)) for colname in colnames]
        formatter.row(rowdata)

class TableFormatter(object):
    # Serves a design spec for making tables (user inheritance to customize)
    def headings(self, headers):
        raise NotImplementedError

    def row(self, rowdata):
        raise NotImplementedError

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for header in headers:
            print('{:>10s}'.format(header), end=' ')
        print()

    def row(self, rowdata):
        for item in rowdata:
            print('{:>10s}'.format(item), end=' ')
        print()

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

