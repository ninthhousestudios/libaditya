starting 287 in vargas.py

                            # have same modality strength, check next level, which is the rashis of the lords of these rashis
                            # 5. If both the Rasis are the same modality, then consider the
                            # lord of the Rasi in the same manner as the Rasi has been considered.
                            # he says "consider the lord of the Rasi in the same manner as the Rashi"
                            # can we consider a Planet in the same way as a Sign? no
                            # a Planet is or is not a karaka, but does not have .how_many_karakas() like Sign
                            # so we need to consider the (two) rāśī of the lords of these two rashis "rāśī adhipatyoḥ imau"
                            # so consider the rashi the lord is in and the rashi the sorted signs lord is in, and which is stronger
                            # therein is the stronger; if this doesn't decide, then go to 6. below
                            signs_lord = sign.lord()
                            signs_Lord = self.planets()[signs_lord] # the Planet class of the lord
                            signs_lords_rashi = self.signs().where_is(signs_lord) # return the Sign class
                            sorted_signs_lord = sorted_sign.lord()
                            sorted_signs_Lord = self.planets()[sorted_signs_lord]
                            sorted_signs_lords_rashi = self.signs().where_is(sorted_signs_lord)
                            # now lets compare their rashis just as we did above

                            if signs_lords_rashi.how_many_karakas() > 0 and sorted_signs_lords_rashi.how_many_karakas() == 0:
                                # sign is stronger than sorted_sign, so put sign at sorted_sign
                                sortedls.insert(n,sign)
                                break # break out of this while loop and go back to the for loop, checking the next sign
                            if signs_lords_rashi.how_many_karakas() > sorted_signs_lords_rashi.how_many_karakas():
                                # sign is stronger, so insert here, then get next sign
                                sortedls.insert(n,sign)
                                break
                            if signs_lords_rashi.how_many_karakas() < sorted_signs_lords_rashi.how_many_karakas():
                                # sign is weaker, so go to next sorted_sign to check that
                                if n == len(sortedls) - 1:
                                # this is the last sign in what we have so far
                                # sign is the weaker, so append it at the end
                                    sortedls.append(sign)
                                    break
                                continue
                            if signs_lords_rashi.how_many_karakas() == sorted_signs_lords_rashi.how_many_karakas():
                                # need to find which planet has the highest dignitiy
                                has_higher = utils.compare_signs_dignities(signs_lords_rashi,sorted_signs_lords_rashi,self.dignities())
                                if has_higher == 1:
                                    # sign is stronger
                                    sortedls.insert(n,sign)
                                    break
                                if has_higher == 2:
                                    # sorted_sign is stronger, so continue this loop to check against the next sign
                                    if n == len(sortedls) - 1:
                                    # this is the last sign in what we have so far
                                    # sign is the weaker, so append it at the end
                                        sortedls.append(sign)
                                        break
                                    continue
                                if has_higher == 0:
                                    # they have the same strength on this level, so we must check other things
                                    # we have to check sign modalities to see which is stronger
                                    # dual strongest, fixed middle, moveable weakest
                                    modality_strength = utils.compare_signs_modalities(signs_lords_rashi,sorted_signs_lords_rashi)
                                    if modality_strength == 1:
                                        # sign is stronger
                                        sortedls.insert(n,sign)
                                        break
                                    if modality_strength == 2:
                                        if n == len(sortedls) - 1:
                                        # this is the last sign in what we have so far
                                        # sign is the weaker, so append it at the end
                                            sortedls.append(sign)
                                            break
                                        continue
                                    if modality_strength == 0:
                                        # 6. if both the lords are the same strong according to the above measures, 
                                        # then the lord who has the highest degrees within the rasi it is in is the stronger, and thus its rasi will be the stronger
                                        if signs_lord.real_in_sign_longitude() == sorted_signs_lord.real_in_sign_longitude():
                                            # this means the lord is the same, so we have to go to the last tier of strength
                                            # so get the two signs of the planet
                                            lords_signs = self.signs().get_signs_of(signs_lord)
                                            if lords_signs[0].sign()%2 == 0:
                                                # even sign
                                                even_sign = lords_signs[0]
                                                odd_sign = lords_signs[1]
                                            else:
                                                even_sign = lords_signs[1]
                                                odd_sign = lords_signs[0]
                                            even_karakas = even_sign.karakas() + self.signs()[even_sign.astrological_signs_forward(2)].karakas() + self.signs()[even_sign.astrological_signs_forward(12)].karakas()
                                            odd_karakas = odd_sign.karakas() + self.signs()[odd_sign.astrological_signs_forward(2)].karakas() + self.signs()[odd_sign.astrological_signs_forward(12)].karakas()
                                            if odd_karakas > even_karakas:
                                                # odd sign is stronger
                                                sortedls.insert(n,sign)
                                                break
                                            else:
                                                sortedls.append(sign)
                                                break
                                        if signs_lord.real_in_sign_longitude() > sorted_signs_lord.real_in_sign_longitude():
                                            sortedls.insert(n,sign)
                                            break
                                        else:
                                            sortedls.append(sign)
                                            break
                                        # if this is equal, then we are dealing with two signs of the same lord
                                        # that are not differentiated by any other qualities, so below is how we do it

                            break
                # if it is not stronger than any, it is weaker than all, so it goes at the end
        return sortedls
