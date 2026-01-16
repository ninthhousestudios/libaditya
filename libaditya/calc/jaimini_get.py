#    This file is part of libaditya.
#
#    Copyright (c) 2025 Josh Harper <humanhaven@substack.com>
#
#    libaditya is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    libaditya is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with libaditya.  If not, see <https://www.gnu.org/licenses/>.


class JaiminiGet:
    """
    a inheritor for calc.Rashi
    defines functions that get certain sets of planets
    """

    def get_spiritual_planets(self,d24=24):
        # for judging personal deity, want 12th from svamsha in d9, d24s, d1
        # get 12th from svamsha in d9,d24,d1
        ak = self.planets().jaimini_karakas()[0]
        d9 = self.master.varga(9)
        d9sign = d9.where_is(ak.identity())
        # forwards or backwards
        sign = 1 if d9sign.sign()%2 == 1 else -1
        d9factor = d9.signs()[d9sign.astrological_signs_forward(12*sign)]

        d24 = self.master.varga(d24)
        d24sign = d24.where_is(ak.identity())
        sign = 1 if d24sign.sign()%2 == 1 else -1
        d24factor = d24.signs()[d24sign.astrological_signs_forward(12*sign)]

        d1sign = self.where_is(ak.identity())
        sign = 1 if d1sign.sign()%2 == 1 else -1
        d1factor = self.signs()[d1sign.astrological_signs_forward(12*sign)]

        d9p = d9factor.grahas()
        d24p = d24factor.grahas()
        d1p = d1factor.grahas()

        print(f"Using {self.context.rashi_aspects} aspects\n")
        if d9p:
            print("Spiritual planets in the d9")
            for p in d9p:
                print(f"{p.name()} ({p.dignity()})")
        if d24p:
            print("Spiritual planets in the d24P")
            for p in d24p:
                print(f"{p.name()} ({p.dignity()})")
        if d1p:
            print("Spiritual planets in the d1")
            for p in d1p:
                print(f"{p.name()} ({p.dignity()})")

        # get planets aspecting
        d9aspecting = d9.signs().rashi_aspects_given_to(d9factor)
        d24aspecting = d24.signs().rashi_aspects_given_to(d24factor)
        d1aspecting = self.signs().rashi_aspects_given_to(d1factor)

        print("\nAspecting planets that may have an influence")
        if d9aspecting:
            print("Aspecting planets in the d9")
            for s in d9aspecting:
                for p in s.grahas():
                    print(f"{p.name()} ({p.dignity()})")
        if d24aspecting:
            print("Aspecting planets in the d24P")
            for s in d24aspecting:
                for p in s.grahas():
                    print(f"{p.name()} ({p.dignity()})")
        if d1aspecting:
            print("Aspecting planets in the d1")
            for s in d1aspecting:
                for p in s.grahas():
                    print(f"{p.name()} ({p.dignity()})")
