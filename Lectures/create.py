import os
import shutil
from datetime import datetime

dates = ['20180104',
         '20180109', '20180111',
         '20180116', '20180118',
         '20180123', '20180125',
         '20180130', '20180201',
         '20180206', '20180208',
         '20180213', '20180215',
         '20180220', '20180222',
         '20180306', '20180308',
         '20180313', '20180315',
         '20180320', '20180322',
         '20180327', '20180329',
         '20180403', '20180405',
         '20180410', '20180412',
         '20180417']

srcdir = 'TEMPLATE'
srcfile = 'TEMPLATE.tex'
origstr = 'January 4, 2018'

for ii, dd in enumerate(dates):
    ll = ii + 1
    dstdir = 'Lecture{:02}_{}'.format(ll, dd)
    dstfile = 'Econ672-Winter2018-Slides-Lecture{:02}.tex'.format(ll)
    shutil.copytree(srcdir, dstdir)
#    shutil.move(dstdir + '/' + srcfile, dstdir + '/' + dstfile)
    datestr = datetime.strptime(dd, '%Y%M%d').strftime('%B %d, %Y')
    with open( os.path.join(dstdir, srcfile), "r" ) as source:
        with open( os.path.join(dstdir, dstfile), "w" ) as target:
            data = source.read()
            changed = data.replace(origstr, datestr)
            target.write(changed)
    os.remove(os.path.join(dstdir, srcfile))
