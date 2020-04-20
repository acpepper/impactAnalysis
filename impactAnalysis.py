import sys
sys.path.append("/home/acpepper/HOTCI_stuff/")
import pyCTH.DataOutBinReader as dor
import pyCTH.HcthReader as hcr
import pyCTH.ImpactAnalysis as ima

# from matplotlib.colors import LinearSegmentedColormap



IMPACT_NAME = "M0.57_m0.47_L0"
# "M1.05_m0.05_L2.7"
# "M0.9_m0.13_L0"
# "M0.75_m0.3_L0"
# "M0.57_m0.47_L0"

IMPACT_DIR = "/group/stewartgrp/acpepper/cthruns/impact_tests/"
if IMPACT_DIR[-1] != '/':
    IMPACT_DIR = IMPACT_DIR+'/'

PLOT_DIR = "../plots/"
if PLOT_DIR[-1] != '/':
    PLOT_DIR = PLOT_DIR+'/'

    

# NOTE: the binary data files are in CGS units
if __name__ == "__main__":
    # plot the energy evolution
    # ima.plotEnergyTotal_dyn(IMPACT_DIR, IMPACT_NAME, "binDat", PLOT_DIR+IMPACT_NAME)
    # ima.plotEnergyTotal_mat(IMPACT_DIR, IMPACT_NAME, "binDat", PLOT_DIR+IMPACT_NAME)

    # plot the angular momentum evolution
    # ima.plotAngMomTotal_dyn(IMPACT_DIR, IMPACT_NAME, "binDat", PLOT_DIR+IMPACT_NAME)
    ima.plotAngMomTotal_mat(IMPACT_DIR, IMPACT_NAME, "binDat", PLOT_DIR+IMPACT_NAME)

    '''
    # binary data analysis (binDat files)
    dodata = dor.DataOutBinReader()
    cycs, numCycs = dodata.getCycles("binDat", IMPACT_DIR+IMPACT_NAME)
    print "Number of cycles = {}".format(len(cycs))
    for cyc in cycs[-1:]:
        dodata = dor.DataOutBinReader()
        dodata.readSev("binDat", cyc, IMPACT_DIR+IMPACT_NAME)
        print "Time of this dump: {} hr".format(dodata.times[0]/3600)
        print dodata.varNames
        # Examine the geometry of the impact
        M_P, R_P, erthInds, diskInds, escpInds = dodata.findPlanet(0)
        p = [0, 0, 0]
        n = [0, 0, 1]
        slcInds = dodata.slice2dFrom3d(p, n, 0)
        ima.plotProfMixing(dodata, PLOT_DIR+IMPACT_NAME)

        # print "mixing slice"
        ima.plotSliceMixing(dodata, PLOT_DIR+IMPACT_NAME, slcInds=slcInds)
        print "dens slice"
        ima.plotSlice(dodata,
                      diskInds,
                      escpInds,
                      R_P,
                      PLOT_DIR+IMPACT_NAME,
                      ("DENS", 1e3),
                      slcInds=slcInds)
        print "press slice"
        ima.plotSlice(dodata,
                      diskInds,
                      escpInds,
                      R_P,
                      PLOT_DIR+IMPACT_NAME,
                      ("P", 0.1),
                      slcInds=slcInds)
        print "temp slice"
        ima.plotSlice(dodata,
                      diskInds,
                      escpInds,
                      R_P,
                      PLOT_DIR+IMPACT_NAME,
                      ("T", 1.1604e4),
                      slcInds=slcInds)
        print "energy scatter"
        ima.plotEnergyScatter(dodata,
                              diskInds,
                              escpInds,
                              M_P,
                              R_P,
                              PLOT_DIR+IMPACT_NAME,
                              slcInds=slcInds)
        print "avels"
        ima.plotAvels(dodata,
                      diskInds,
                      escpInds,
                      M_P,
                      R_P,
                      PLOT_DIR+IMPACT_NAME,
                      slcInds=slcInds)
        '''
