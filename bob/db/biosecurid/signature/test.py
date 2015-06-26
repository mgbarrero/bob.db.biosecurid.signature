#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""A few checks at the Biosecurid database.
"""

import os, sys
import unittest
import bob.db.biosecurid.signature

class BiosecuridDatabaseTest(unittest.TestCase):
  """Performs various tests on the Biosecurid database."""

  def test01_clients(self):
    db = bob.db.biosecurid.signature.Database()
    self.assertEqual(len(db.groups()), 3)
    self.assertEqual(len(db.clients()), 800)
    self.assertEqual(len(db.clients(groups='dev')), 300)
    self.assertEqual(len(db.clients(groups='eval')), 200)
    self.assertEqual(len(db.clients(groups='world')), 300)
    self.assertEqual(len(db.clients(groups='dev', types='Genuine')), 150)
    self.assertEqual(len(db.clients(groups='eval', types='Genuine')), 100)
    self.assertEqual(len(db.clients(groups='world', types='Genuine')), 150)
    self.assertEqual(len(db.clients(groups='impostorDev', types='Genuine')), 12)
    self.assertEqual(len(db.clients(groups='impostorEval', types='Genuine')), 10)
    self.assertEqual(len(db.models()), 228)
    self.assertEqual(len(db.models(groups='dev')), 138)
    self.assertEqual(len(db.models(groups='eval')), 90)


  def test02_objects(self):
    db = bob.db.biosecurid.signature.Database()
    self.assertEqual(len(db.objects()), 9136)#11200
    # A
    self.assertEqual(len(db.objects(protocol='A')), 9136)
    self.assertEqual(len(db.objects(protocol='A', groups='world')), 2400)
    
    self.assertEqual(len(db.objects(protocol='A', groups='dev')), 4056)
    self.assertEqual(len(db.objects(protocol='A', groups='dev', purposes='enrol')), 1104)
    self.assertEqual(len(db.objects(protocol='A', groups='dev', purposes='probe')), 2952)
    self.assertEqual(len(db.objects(protocol='A', groups='dev', purposes='probe', classes='client')), 2760)
    self.assertEqual(len(db.objects(protocol='A', groups='dev', purposes='probe', classes='impostor')), 192)
    self.assertEqual(len(db.objects(protocol='A', groups='dev', purposes='probe', model_ids=['Genuine_1151'], classes='client')), 8)
    self.assertEqual(len(db.objects(protocol='A', groups='dev', purposes='probe', model_ids=['Impostor_1151'], classes='client')), 12)
    self.assertEqual(len(db.objects(protocol='A', groups='dev', purposes='probe', model_ids=['Genuine_1151'], classes='impostor')), 192)
    self.assertEqual(len(db.objects(protocol='A', groups='dev', purposes='probe', model_ids=['Genuine_1151','Genuine_1152'], classes='client')), 16)
    self.assertEqual(len(db.objects(protocol='A', groups='dev', purposes='probe', model_ids=['Impostor_1151','Impostor_1152'], classes='client')), 24)
    self.assertEqual(len(db.objects(protocol='A', groups='dev', purposes='probe', model_ids=['Genuine_1151','Genuine_1152'], classes='impostor')), 192)
    
    self.assertEqual(len(db.objects(protocol='A', groups='eval')), 2680)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='enrol')), 720)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='probe')), 1960)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='probe', classes='client')), 1800)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='probe', classes='impostor')), 160)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='probe', model_ids=['Genuine_1301'], classes='client')), 8)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='probe', model_ids=['Impostor_1301'], classes='client')), 12)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='probe', model_ids=['Genuine_1301'], classes='impostor')), 160)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='probe', model_ids=['Genuine_1301','Genuine_1302'], classes='client')), 16)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='probe', model_ids=['Impostor_1301','Impostor_1302'], classes='client')), 24)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='probe', model_ids=['Genuine_1301','Genuine_1302'], classes='impostor')), 160)






  def test03_driver_api(self):

    from bob.db.base.script.dbmanage import main
    self.assertEqual(main('biosecurid.signature dumplist --self-test'.split()), 0)
    self.assertEqual(main('biosecurid.signature checkfiles --self-test'.split()), 0)
    self.assertEqual(main('biosecurid.signature reverse user1001/session0001/u1001s0001_sg0001 --self-test'.split()), 0)
    self.assertEqual(main('biosecurid.signature path 3011 --self-test'.split()), 0)

