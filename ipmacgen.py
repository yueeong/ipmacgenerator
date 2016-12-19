    def gen_ipmac_pair(mac_prefix='00:00:6a:43', ip_prefix='156.146', start_mac='00:01', start_ip='1.1'):
        '''
        This is a ip-mac address pair never ending generator.

        :param mac_prefix:
        :param ip_prefix:
        :param start_mac:
        :param start_ip:
        :return:
        '''
        # mac generators section
        firstoct = int(start_mac.split(':')[1], 16)
        secondoct = int(start_mac.split(':')[0], 16)

        def oct_gen(start):
            x = start
            while True:
                yield '{num:02x}'.format(num=x)
                x += 1
                if x == 256:
                    x = 0

        def s_gen(secondoct):
            oca = oct_gen(firstoct)
            while True:
                pxxp = next(oca)
                if pxxp == '00':
                    secondoct += 1
                yield '{num:02x}'.format(num=secondoct) + ':' + str(pxxp)

        # ip generators section
        firstipoct = int(start_ip.split('.')[1])
        secondipoct = int(start_ip.split('.')[0])

        def p_gen(start):
            x = start
            while True:
                yield x
                x += 1
                if x == 256:
                    x = 0

        def r_gen(secondipoct):
            pca = p_gen(firstipoct)
            while True:
                pup = next(pca)
                if pup == 0:
                    secondipoct += 1
                yield str(secondipoct) + '.' + str(pup)

        # Make the dictionary
        mac_suffix = s_gen(secondoct)
        ip_suffix = r_gen(secondipoct)

        while True:
            yield (str(ip_prefix) + '.' + next(ip_suffix), str(mac_prefix) + ':' + next(mac_suffix))
