/*
 * ussim.java
 */

import com.comsol.model.*;
import com.comsol.model.util.*;

/** Model exported on Jul 26 2021, 15:06 by COMSOL 5.6.0.341. */
public class ussim {

  public static Model run() {
    Model model = ModelUtil.create("Model");

    model.modelPath("C:\\Users\\ssolmaz\\Desktop\\comsol_new\\comsol");

    model.label("ussim.mph");

    model.param().set("L", "140 [mm]", "Bath length");
    model.param().set("W", "50 [mm]", "Bath width");
    model.param().set("H", "60 [mm]", "Bath height");
    model.param().set("f", "27.2 [kHz]", "Ultrasound frequency");
    model.param().set("c_w", "1500 [m/s]", "Speed of soun in water");
    model.param().set("rho_w", "1000 [kg/m^3]", "Density of water");
    model.param().set("x_Tr", "93 [mm]", "X-coordinate transducer");
    model.param().set("P_t", "65 [W]", "Power input");
    model.param().set("R_t", "22 [mm]", "Transducer radius");
    model.param().set("A_t", "pi*R_t^2", "Transducer cross section");
    model.param().set("n", "15", "Number of mesh elements per wavelength");

    model.component().create("comp1", true);

    model.component("comp1").geom().create("geom1", 3);

    model.result().table().create("tbl1", "Table");
    model.result().table().create("tbl2", "Table");
    model.result().table().create("tbl3", "Table");
    model.result().table().create("tbl4", "Table");

    model.component("comp1").mesh().create("mesh1");

    model.component("comp1").geom("geom1").geomRep("comsol");
    model.component("comp1").geom("geom1").create("blk1", "Block");
    model.component("comp1").geom("geom1").feature("blk1").set("size", new String[]{"L", "W", "H"});
    model.component("comp1").geom("geom1").create("cyl1", "Cylinder");
    model.component("comp1").geom("geom1").feature("cyl1").set("pos", new String[]{"x_Tr", "W/2", "-0.005"});
    model.component("comp1").geom("geom1").feature("cyl1").set("r", "R_t");
    model.component("comp1").geom("geom1").feature("cyl1").set("h", 0.005);
    model.component("comp1").geom("geom1").create("dif1", "Difference");
    model.component("comp1").geom("geom1").feature("dif1").selection("input").set("blk1");
    model.component("comp1").geom("geom1").feature("dif1").selection("input2").set("cyl1");
    model.component("comp1").geom("geom1").run();
    model.component("comp1").geom("geom1").run("fin");

    model.component("comp1").material().create("mat1", "Common");
    model.component("comp1").material("mat1").propertyGroup("def").func().create("eta", "Piecewise");
    model.component("comp1").material("mat1").propertyGroup("def").func().create("Cp", "Piecewise");
    model.component("comp1").material("mat1").propertyGroup("def").func().create("rho", "Piecewise");
    model.component("comp1").material("mat1").propertyGroup("def").func().create("k", "Piecewise");
    model.component("comp1").material("mat1").propertyGroup("def").func().create("cs", "Interpolation");
    model.component("comp1").material("mat1").propertyGroup("def").func().create("an1", "Analytic");
    model.component("comp1").material("mat1").propertyGroup("def").func().create("an2", "Analytic");
    model.component("comp1").material("mat1").propertyGroup("def").func().create("an3", "Analytic");

    model.component("comp1").physics().create("acpr", "PressureAcoustics", "geom1");
    model.component("comp1").physics("acpr").create("pr1", "Pressure", 2);
    model.component("comp1").physics("acpr").feature("pr1").selection().set(6);
    model.component("comp1").physics("acpr").create("ssb1", "SoundSoft", 2);
    model.component("comp1").physics("acpr").feature("ssb1").selection().set(1, 2, 3, 4, 5, 7);

    model.component("comp1").mesh("mesh1").create("ftet1", "FreeTet");

    model.result().table("tbl1").comments("Global Evaluation 1");
    model.result().table("tbl2").comments("Volume Integration 1");
    model.result().table("tbl3").comments("Global Evaluation 1");
    model.result().table("tbl4").comments("Volume Average 1");

    model.component("comp1").material("mat1").label("Water, liquid");
    model.component("comp1").material("mat1").set("family", "water");
    model.component("comp1").material("mat1").propertyGroup("def").func("eta").set("arg", "T");
    model.component("comp1").material("mat1").propertyGroup("def").func("eta")
         .set("pieces", new String[][]{{"273.15", "413.15", "1.3799566804-0.021224019151*T^1+1.3604562827E-4*T^2-4.6454090319E-7*T^3+8.9042735735E-10*T^4-9.0790692686E-13*T^5+3.8457331488E-16*T^6"}, {"413.15", "553.75", "0.00401235783-2.10746715E-5*T^1+3.85772275E-8*T^2-2.39730284E-11*T^3"}});
    model.component("comp1").material("mat1").propertyGroup("def").func("eta").set("argunit", "K");
    model.component("comp1").material("mat1").propertyGroup("def").func("eta").set("fununit", "Pa*s");
    model.component("comp1").material("mat1").propertyGroup("def").func("Cp").set("arg", "T");
    model.component("comp1").material("mat1").propertyGroup("def").func("Cp")
         .set("pieces", new String[][]{{"273.15", "553.75", "12010.1471-80.4072879*T^1+0.309866854*T^2-5.38186884E-4*T^3+3.62536437E-7*T^4"}});
    model.component("comp1").material("mat1").propertyGroup("def").func("Cp").set("argunit", "K");
    model.component("comp1").material("mat1").propertyGroup("def").func("Cp").set("fununit", "J/(kg*K)");
    model.component("comp1").material("mat1").propertyGroup("def").func("rho").set("arg", "T");
    model.component("comp1").material("mat1").propertyGroup("def").func("rho").set("smooth", "contd1");
    model.component("comp1").material("mat1").propertyGroup("def").func("rho")
         .set("pieces", new String[][]{{"273.15", "293.15", "0.000063092789034*T^3-0.060367639882855*T^2+18.9229382407066*T-950.704055329848"}, {"293.15", "373.15", "0.000010335053319*T^3-0.013395065634452*T^2+4.969288832655160*T+432.257114008512"}});
    model.component("comp1").material("mat1").propertyGroup("def").func("rho").set("argunit", "K");
    model.component("comp1").material("mat1").propertyGroup("def").func("rho").set("fununit", "kg/m^3");
    model.component("comp1").material("mat1").propertyGroup("def").func("k").set("arg", "T");
    model.component("comp1").material("mat1").propertyGroup("def").func("k")
         .set("pieces", new String[][]{{"273.15", "553.75", "-0.869083936+0.00894880345*T^1-1.58366345E-5*T^2+7.97543259E-9*T^3"}});
    model.component("comp1").material("mat1").propertyGroup("def").func("k").set("argunit", "K");
    model.component("comp1").material("mat1").propertyGroup("def").func("k").set("fununit", "W/(m*K)");
    model.component("comp1").material("mat1").propertyGroup("def").func("cs")
         .set("table", new String[][]{{"273", "1403"}, 
         {"278", "1427"}, 
         {"283", "1447"}, 
         {"293", "1481"}, 
         {"303", "1507"}, 
         {"313", "1526"}, 
         {"323", "1541"}, 
         {"333", "1552"}, 
         {"343", "1555"}, 
         {"353", "1555"}, 
         {"363", "1550"}, 
         {"373", "1543"}});
    model.component("comp1").material("mat1").propertyGroup("def").func("cs").set("interp", "piecewisecubic");
    model.component("comp1").material("mat1").propertyGroup("def").func("cs").set("argunit", "K");
    model.component("comp1").material("mat1").propertyGroup("def").func("cs").set("fununit", "m/s");
    model.component("comp1").material("mat1").propertyGroup("def").func("an1").set("funcname", "alpha_p");
    model.component("comp1").material("mat1").propertyGroup("def").func("an1").set("expr", "-1/rho(T)*d(rho(T),T)");
    model.component("comp1").material("mat1").propertyGroup("def").func("an1").set("args", new String[]{"T"});
    model.component("comp1").material("mat1").propertyGroup("def").func("an1").set("argunit", "K");
    model.component("comp1").material("mat1").propertyGroup("def").func("an1").set("fununit", "1/K");
    model.component("comp1").material("mat1").propertyGroup("def").func("an1")
         .set("plotargs", new String[][]{{"T", "273.15", "373.15"}});
    model.component("comp1").material("mat1").propertyGroup("def").func("an2").set("funcname", "gamma_w");
    model.component("comp1").material("mat1").propertyGroup("def").func("an2")
         .set("expr", "1+(T/Cp(T))*(alpha_p(T)*cs(T))^2");
    model.component("comp1").material("mat1").propertyGroup("def").func("an2").set("args", new String[]{"T"});
    model.component("comp1").material("mat1").propertyGroup("def").func("an2").set("argunit", "K");
    model.component("comp1").material("mat1").propertyGroup("def").func("an2").set("fununit", "1");
    model.component("comp1").material("mat1").propertyGroup("def").func("an2")
         .set("plotargs", new String[][]{{"T", "273.15", "373.15"}});
    model.component("comp1").material("mat1").propertyGroup("def").func("an3").set("funcname", "muB");
    model.component("comp1").material("mat1").propertyGroup("def").func("an3").set("expr", "2.79*eta(T)");
    model.component("comp1").material("mat1").propertyGroup("def").func("an3").set("args", new String[]{"T"});
    model.component("comp1").material("mat1").propertyGroup("def").func("an3").set("argunit", "K");
    model.component("comp1").material("mat1").propertyGroup("def").func("an3").set("fununit", "Pa*s");
    model.component("comp1").material("mat1").propertyGroup("def").func("an3")
         .set("plotargs", new String[][]{{"T", "273.15", "553.75"}});
    model.component("comp1").material("mat1").propertyGroup("def").set("thermalexpansioncoefficient", "");
    model.component("comp1").material("mat1").propertyGroup("def").set("bulkviscosity", "");
    model.component("comp1").material("mat1").propertyGroup("def")
         .set("thermalexpansioncoefficient", new String[]{"alpha_p(T)", "0", "0", "0", "alpha_p(T)", "0", "0", "0", "alpha_p(T)"});
    model.component("comp1").material("mat1").propertyGroup("def").set("bulkviscosity", "muB(T)");
    model.component("comp1").material("mat1").propertyGroup("def").set("dynamicviscosity", "eta(T)");
    model.component("comp1").material("mat1").propertyGroup("def").set("ratioofspecificheat", "gamma_w(T)");
    model.component("comp1").material("mat1").propertyGroup("def")
         .set("electricconductivity", new String[]{"5.5e-6[S/m]", "0", "0", "0", "5.5e-6[S/m]", "0", "0", "0", "5.5e-6[S/m]"});
    model.component("comp1").material("mat1").propertyGroup("def").set("heatcapacity", "Cp(T)");
    model.component("comp1").material("mat1").propertyGroup("def").set("density", "rho(T)");
    model.component("comp1").material("mat1").propertyGroup("def")
         .set("thermalconductivity", new String[]{"k(T)", "0", "0", "0", "k(T)", "0", "0", "0", "k(T)"});
    model.component("comp1").material("mat1").propertyGroup("def").set("soundspeed", "cs(T)");
    model.component("comp1").material("mat1").propertyGroup("def").addInput("temperature");

    model.component("comp1").physics("acpr").feature("fpam1").set("minput_practicalsalinity", "1000*0");
    model.component("comp1").physics("acpr").feature("pr1").set("p0", "(2*rho_w*c_w*P_t/A_t)^(1/2)");

    model.component("comp1").mesh("mesh1").feature("size").set("custom", "on");
    model.component("comp1").mesh("mesh1").feature("size").set("hmax", "c_w/f/n");
    model.component("comp1").mesh("mesh1").feature("size").set("hmin", "c_w/f/(n+1)");
    model.component("comp1").mesh("mesh1").feature("ftet1").set("optcurved", false);
    model.component("comp1").mesh("mesh1").run();

    model.study().create("std1");
    model.study("std1").create("freq", "Frequency");

    model.sol().create("sol1");
    model.sol("sol1").study("std1");
    model.sol("sol1").attach("std1");
    model.sol("sol1").create("st1", "StudyStep");
    model.sol("sol1").create("v1", "Variables");
    model.sol("sol1").create("s1", "Stationary");
    model.sol("sol1").feature("s1").create("p1", "Parametric");
    model.sol("sol1").feature("s1").create("fc1", "FullyCoupled");
    model.sol("sol1").feature("s1").create("d1", "Direct");
    model.sol("sol1").feature("s1").create("i1", "Iterative");
    model.sol("sol1").feature("s1").create("i2", "Iterative");
    model.sol("sol1").feature("s1").create("i3", "Iterative");
    model.sol("sol1").feature("s1").create("i4", "Iterative");
    model.sol("sol1").feature("s1").feature("i1").create("mg1", "Multigrid");
    model.sol("sol1").feature("s1").feature("i2").create("mg1", "Multigrid");
    model.sol("sol1").feature("s1").feature("i3").create("mg1", "Multigrid");
    model.sol("sol1").feature("s1").feature("i4").create("dd1", "DomainDecompositionSchur");
    model.sol("sol1").feature("s1").feature("i4").feature("dd1").feature("ds").create("d1", "Direct");
    model.sol("sol1").feature("s1").feature("i4").feature("dd1").feature("ssso")
         .create("sskr1", "SchurSourceKrylovPreconditioner");
    model.sol("sol1").feature("s1").feature().remove("fcDef");

    model.result().create("pg1", "PlotGroup3D");
    model.result().create("pg2", "PlotGroup3D");
    model.result().create("pg3", "PlotGroup3D");
    model.result("pg1").create("surf1", "Surface");
    model.result("pg1").create("slc1", "Slice");
    model.result("pg1").feature("surf1").set("data", "dset1");
    model.result("pg1").feature("slc1").set("expr", "abs(acpr.p_t)");
    model.result("pg2").create("surf1", "Surface");
    model.result("pg2").feature("surf1").set("expr", "acpr.Lp");
    model.result("pg3").create("iso1", "Isosurface");
    model.result().export().create("plot1", "Plot");
    model.result().export().create("plot2", "Plot");
    model.result().export().create("data1", "Data");

    model.study("std1").feature("freq").set("plist", "f");

    model.sol("sol1").attach("std1");
    model.sol("sol1").feature("st1").label("Compile Equations: Frequency Domain");
    model.sol("sol1").feature("v1").label("Dependent Variables 1.1");
    model.sol("sol1").feature("v1").set("clistctrl", new String[]{"p1"});
    model.sol("sol1").feature("v1").set("cname", new String[]{"freq"});
    model.sol("sol1").feature("v1").set("clist", new String[]{"f"});
    model.sol("sol1").feature("s1").label("Stationary Solver 1.1");
    model.sol("sol1").feature("s1").feature("dDef").label("Direct 2");
    model.sol("sol1").feature("s1").feature("aDef").label("Advanced 1");
    model.sol("sol1").feature("s1").feature("aDef").set("complexfun", true);
    model.sol("sol1").feature("s1").feature("p1").label("Parametric 1.1");
    model.sol("sol1").feature("s1").feature("p1").set("pname", new String[]{"freq"});
    model.sol("sol1").feature("s1").feature("p1").set("plistarr", new String[]{"f"});
    model.sol("sol1").feature("s1").feature("p1").set("punit", new String[]{"Hz"});
    model.sol("sol1").feature("s1").feature("p1").set("pcontinuationmode", "no");
    model.sol("sol1").feature("s1").feature("p1").set("preusesol", "auto");
    model.sol("sol1").feature("s1").feature("fc1").label("Fully Coupled 1.1");
    model.sol("sol1").feature("s1").feature("fc1").set("linsolver", "d1");
    model.sol("sol1").feature("s1").feature("d1").label("Suggested Direct Solver (acpr)");
    model.sol("sol1").feature("s1").feature("i1").label("Suggested Iterative Solver (GMRES with GMG) (acpr)");
    model.sol("sol1").feature("s1").feature("i1").feature("ilDef").label("Incomplete LU 1");
    model.sol("sol1").feature("s1").feature("i1").feature("mg1").label("Multigrid 1.1");
    model.sol("sol1").feature("s1").feature("i1").feature("mg1").feature("pr").label("Presmoother 1");
    model.sol("sol1").feature("s1").feature("i1").feature("mg1").feature("pr").feature("soDef").label("SOR 1");
    model.sol("sol1").feature("s1").feature("i1").feature("mg1").feature("po").label("Postsmoother 1");
    model.sol("sol1").feature("s1").feature("i1").feature("mg1").feature("po").feature("soDef").label("SOR 1");
    model.sol("sol1").feature("s1").feature("i1").feature("mg1").feature("cs").label("Coarse Solver 1");
    model.sol("sol1").feature("s1").feature("i1").feature("mg1").feature("cs").feature("dDef").label("Direct 1");
    model.sol("sol1").feature("s1").feature("i2").label("Suggested Iterative Solver (FGMRES with GMG) (acpr)");
    model.sol("sol1").feature("s1").feature("i2").set("linsolver", "fgmres");
    model.sol("sol1").feature("s1").feature("i2").feature("ilDef").label("Incomplete LU 1");
    model.sol("sol1").feature("s1").feature("i2").feature("mg1").label("Multigrid 1.1");
    model.sol("sol1").feature("s1").feature("i2").feature("mg1").feature("pr").label("Presmoother 1");
    model.sol("sol1").feature("s1").feature("i2").feature("mg1").feature("pr").feature("soDef").label("SOR 1");
    model.sol("sol1").feature("s1").feature("i2").feature("mg1").feature("po").label("Postsmoother 1");
    model.sol("sol1").feature("s1").feature("i2").feature("mg1").feature("po").feature("soDef").label("SOR 1");
    model.sol("sol1").feature("s1").feature("i2").feature("mg1").feature("cs").label("Coarse Solver 1");
    model.sol("sol1").feature("s1").feature("i2").feature("mg1").feature("cs").feature("dDef").label("Direct 1");
    model.sol("sol1").feature("s1").feature("i3").label("Suggested Iterative Solver (Shifted Laplace) (acpr)");
    model.sol("sol1").feature("s1").feature("i3").feature("ilDef").label("Incomplete LU 1");
    model.sol("sol1").feature("s1").feature("i3").feature("mg1").label("Multigrid 1.1");
    model.sol("sol1").feature("s1").feature("i3").feature("mg1").set("mcasegen", "coarse");
    model.sol("sol1").feature("s1").feature("i3").feature("mg1").set("scale", 3);
    model.sol("sol1").feature("s1").feature("i3").feature("mg1").set("prefermatfree", true);
    model.sol("sol1").feature("s1").feature("i3").feature("mg1").set("slaplacemain", true);
    model.sol("sol1").feature("s1").feature("i3").feature("mg1").set("epsslaplacemain", new String[]{"acpr", "0.4"});
    model.sol("sol1").feature("s1").feature("i3").feature("mg1").set("slaplacegmg", true);
    model.sol("sol1").feature("s1").feature("i3").feature("mg1").set("epsslaplacegmg", new String[]{"acpr", "0.4"});
    model.sol("sol1").feature("s1").feature("i3").feature("mg1").feature("pr").label("Presmoother 1");
    model.sol("sol1").feature("s1").feature("i3").feature("mg1").feature("pr").feature("soDef").label("SOR 1");
    model.sol("sol1").feature("s1").feature("i3").feature("mg1").feature("po").label("Postsmoother 1");
    model.sol("sol1").feature("s1").feature("i3").feature("mg1").feature("po").feature("soDef").label("SOR 1");
    model.sol("sol1").feature("s1").feature("i3").feature("mg1").feature("cs").label("Coarse Solver 1");
    model.sol("sol1").feature("s1").feature("i3").feature("mg1").feature("cs").feature("dDef").label("Direct 1");
    model.sol("sol1").feature("s1").feature("i4").label("Suggested Iterative Solver (Domain Decomposition) (acpr)");
    model.sol("sol1").feature("s1").feature("i4").set("linsolver", "fgmres");
    model.sol("sol1").feature("s1").feature("i4").feature("ilDef").label("Incomplete LU 1");
    model.sol("sol1").feature("s1").feature("i4").feature("dd1").label("Domain Decomposition (Schur) 1.1");
    model.sol("sol1").feature("s1").feature("i4").feature("dd1").set("dompernodemaxactive", true);
    model.sol("sol1").feature("s1").feature("i4").feature("dd1").set("prefermatfree", true);
    model.sol("sol1").feature("s1").feature("i4").feature("dd1").set("ddboundary", "absorbing");
    model.sol("sol1").feature("s1").feature("i4").feature("dd1").set("alphaabsorbing", new String[]{"acpr", "1"});
    model.sol("sol1").feature("s1").feature("i4").feature("dd1")
         .set("sndorderabsorbing", new String[]{"acpr", "on"});
    model.sol("sol1").feature("s1").feature("i4").feature("dd1").set("betaabsorbing", new String[]{"acpr", "0.01"});
    model.sol("sol1").feature("s1").feature("i4").feature("dd1").feature("sso").label("Schur Solver 1");
    model.sol("sol1").feature("s1").feature("i4").feature("dd1").feature("sso").feature("skrDef")
         .label("Krylov Preconditioner 1");
    model.sol("sol1").feature("s1").feature("i4").feature("dd1").feature("sso").feature("skrDef").feature("sloDef")
         .label("Localized Schur 1");
    model.sol("sol1").feature("s1").feature("i4").feature("dd1").feature("ds").label("Domain Solver 1");
    model.sol("sol1").feature("s1").feature("i4").feature("dd1").feature("ds").feature("dDef").label("Direct 2");
    model.sol("sol1").feature("s1").feature("i4").feature("dd1").feature("ds").feature("d1").label("Direct 1.1");
    model.sol("sol1").feature("s1").feature("i4").feature("dd1").feature("ds").feature("d1").set("mumpsblr", true);
    model.sol("sol1").feature("s1").feature("i4").feature("dd1").feature("ds").feature("d1")
         .set("mumpsblrtol", "1.0E-3");
    model.sol("sol1").feature("s1").feature("i4").feature("dd1").feature("ssso").label("Schur Source Solver 1");
    model.sol("sol1").feature("s1").feature("i4").feature("dd1").feature("ssso").feature("sskrDef")
         .label("Krylov Preconditioner 2");
    model.sol("sol1").feature("s1").feature("i4").feature("dd1").feature("ssso").feature("sskr1")
         .label("Krylov Preconditioner 1.1");
    model.sol("sol1").feature("s1").feature("i4").feature("dd1").feature("ssso").feature("sskr1")
         .set("itrestart", 100);
    model.sol("sol1").feature("s1").feature("i4").feature("dd1").feature("ssso").feature("sskr1")
         .set("itol", "1.0E-1");
    model.sol("sol1").runAll();

    model.result("pg1").label("Acoustic Pressure (acpr)");
    model.result("pg1").feature("surf1").set("descr", "Total acoustic pressure field");
    model.result("pg1").feature("surf1").set("colortable", "Wave");
    model.result("pg1").feature("surf1").set("colortablesym", true);
    model.result("pg1").feature("surf1").set("resolution", "normal");
    model.result("pg1").feature("slc1").label("Plane through middle");
    model.result("pg1").feature("slc1").set("quickplane", "zx");
    model.result("pg1").feature("slc1").set("quickymethod", "coord");
    model.result("pg1").feature("slc1").set("quicky", "W/2");
    model.result("pg1").feature("slc1").set("resolution", "normal");
    model.result("pg2").label("Sound Pressure Level (acpr)");
    model.result("pg2").feature("surf1").set("descr", "Sound pressure level");
    model.result("pg2").feature("surf1").set("resolution", "normal");
    model.result("pg3").label("Acoustic Pressure, Isosurfaces (acpr)");
    model.result("pg3").feature("iso1").set("descr", "Total acoustic pressure field");
    model.result("pg3").feature("iso1").set("number", 10);
    model.result("pg3").feature("iso1").set("colortable", "Wave");
    model.result("pg3").feature("iso1").set("colortablesym", true);
    model.result("pg3").feature("iso1").set("resolution", "normal");
    model.result().export("plot1").set("exporttype", "vtu");
    model.result().export("plot1").set("filename", "C:\\Users\\ssolmaz\\Desktop\\comsol_new\\comsol\\pressure.vtu");
    model.result().export("plot2").set("exporttype", "vtu");
    model.result().export("plot2").set("filename", "C:\\Users\\ssolmaz\\Desktop\\comsol_new\\comsol\\press.vtu");
    model.result().export("data1").set("exporttype", "vtu");
    model.result().export("data1").set("filename", "C:\\Users\\ssolmaz\\Desktop\\comsol_new\\comsol\\volume.vtu");

    model.label("ussim.mph");

    model.result().export("plot1").run();
    model.result().export("plot2").run();
    model.result().export("data1").run();

    return model;
  }

  public static void main(String[] args) {
    run();
  }

}
