import numpy as np
import PMT as pmt
import matplotlib.pyplot as plt

nsamp = [100, 100, 100]
tsamp = 0.01
nrep = 2

k = np.arange(nrep) + 1

stds = []
means = []
o = 1
plt.clf()
#plt.suptitle('Different sample sizes - 100, 500 and 1000 samples (1ms)')

for indx in range(len(nsamp)):
    for i in k:
        print nsamp[indx]
        myfilename = 'section6_{0}_{1}_{2}.dat'.format(i,tsamp,nsamp[indx])
        x = pmt.photoncount(tsamp, nsamp[indx])
        print np.mean(x), np.std(x)
        stds.append(np.std(x))
        means.append(np.mean(x))
        print "Writing data to " + myfilename

        np.savetxt(myfilename, x, fmt='%i')



        hmin = 0
        hmax = np.max(x) + 1
        hr = np.arange(hmin, hmax+1)
        hist = np.array([np.where(x==indx1)[0].size for indx1 in hr])
        plt.subplot(3,2,o)
        plt.title('Photons per 0.1ms (%s samples)' % (nsamp[indx]), fontsize=10)
        o += 1
        plt.plot(hr, hist, drawstyle='steps-mid')
        plt.ylabel('Frequency')
        plt.xlabel('Count')
plt.tight_layout()
