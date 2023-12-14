11-17 15:54:42.228   442   442 D XposedStartupMarker: Current time: 1479378282, PID: 442
11-17 15:54:42.228   442   442 I Xposed  : -----------------
11-17 15:54:42.228   442   442 I Xposed  : Starting Xposed version 86, compiled for SDK 23
11-17 15:54:42.228   442   442 I Xposed  : Device: Nexus 7 (asus), Android version 6.0.1 (SDK 23)
11-17 15:54:42.228   442   442 I Xposed  : ROM: cm_deb-userdebug 6.0.1 MOB31K 4fbf2568fa test-keys
11-17 15:54:42.228   442   442 I Xposed  : Build fingerprint: google/razorg/deb:6.0.1/MOB30X/3036618:user/release-keys
11-17 15:54:42.229   442   442 I Xposed  : Platform: armeabi-v7a, 32-bit binary, system server: yes
11-17 15:54:42.229   442   442 I Xposed  : SELinux enabled: yes, enforcing: yes
11-17 15:54:42.272   822   822 I ServiceManager: Waiting for service user.xposed.system...
11-17 15:54:43.297   442   442 I Xposed  : -----------------
11-17 15:54:43.297   442   442 I Xposed  : Added Xposed (/system/framework/XposedBridge.jar) to CLASSPATH
11-17 15:54:43.297   442   442 D AndroidRuntime: >>>>>> START de.robv.android.xposed.XposedBridge uid 0 <<<<<<
11-17 15:55:18.850  1155  1155 I dex2oat : /system/bin/dex2oat --dex-file=/system/framework/XposedBridge.jar --oat-file=/data/dalvik-cache/arm/system@framework@XposedBridge.jar@classes.dex
11-17 15:55:19.298   442   442 I Xposed  : Detected ART runtime
11-17 15:55:19.303   442   442 I Xposed  : Found Xposed class 'de/robv/android/xposed/XposedBridge', now initializing
11-17 15:55:19.688  1179  1179 I dex2oat : /system/bin/dex2oat --dex-file=/data/dalvik-cache/xposed_XResourcesSuperClass.dex --oat-file=/data/dalvik-cache/arm/data@dalvik-cache@xposed_XResourcesSuperClass.dex
11-17 15:56:24.090  1185  1185 W PackageManager: Not granting permission android.permission.WRITE_EXTERNAL_STORAGE to package de.robv.android.xposed.installer because it was previously installed without
11-17 15:56:24.090  1185  1185 W PackageManager: Not granting permission android.permission.READ_EXTERNAL_STORAGE to package de.robv.android.xposed.installer because it was previously installed without
11-17 15:56:24.910  1185  1856 W PackageManager: Not granting permission android.permission.WRITE_EXTERNAL_STORAGE to package de.robv.android.xposed.installer because it was previously installed without
11-17 15:56:24.910  1185  1856 W PackageManager: Not granting permission android.permission.READ_EXTERNAL_STORAGE to package de.robv.android.xposed.installer because it was previously installed without
11-17 16:05:05.897  1185  1185 I PackageManager.DexOptimizer: Running dexopt (dex2oat) on: /data/app/de.robv.android.xposed.installer-1/base.apk pkg=de.robv.android.xposed.installer isa=arm vmSafeMode=false debuggable=false oatDir = /data/app/de.robv.android.xposed.installer-1/oat bootComplete=false
11-17 16:06:00.585  4082  4082 W art     : Failed execv(/system/bin/dex2oat --runtime-arg -classpath --runtime-arg /system/framework/XposedBridge.jar --instruction-set=arm --instruction-set-features=smp,-div,-atomic_ldrd_strd --runtime-arg -Xnorelocate --boot-image=/system/framework/boot.art --runtime-arg -Xms64m --runtime-arg -Xmx512m --instruction-set-variant=krait --instruction-set-features=default --dex-file=/data/data/com.google.android.gms/app_chimera/m/00000014/oat/arm/DynamiteModulesA_GmsCore_prodmnc_xhdpi_release.odex --oat-file=/data/dalvik-cache/arm/data@data@com.google.android.gms@app_chimera@m@00000014@DynamiteModulesA_GmsCore_prodmnc_xhdpi_release.apk@classes.dex) because non-0 exit status
11-17 16:06:04.480  4736  4736 D StrictMode: 	at de.robv.android.xposed.XposedInit$7.afterHookedMethod(XposedInit.java:269)
11-17 16:06:04.480  4736  4736 D StrictMode: 	at de.robv.android.xposed.XposedBridge.handleHookedMethod(XposedBridge.java:348)
11-17 16:06:04.480  4736  4736 D StrictMode: 	at android.app.ResourcesManager.getTopLevelResources(<Xposed>)
11-17 16:06:04.480  4736  4736 D StrictMode: 	at de.robv.android.xposed.XposedBridge.invokeOriginalMethodNative(Native Method)
11-17 16:06:04.480  4736  4736 D StrictMode: 	at de.robv.android.xposed.XposedBridge.handleHookedMethod(XposedBridge.java:334)
11-17 16:06:04.480  4736  4736 D StrictMode: 	at android.app.ActivityThread.handleBindApplication(<Xposed>)
11-17 16:06:04.480  4736  4736 D StrictMode: 	at de.robv.android.xposed.XposedBridge.main(XposedBridge.java:102)
11-17 16:06:06.804  3898  3898 W Resources: 	at de.robv.android.xposed.XposedBridge.main(XposedBridge.java:102)
11-17 16:06:08.476  4957  5271 W art     : Failed execv(/system/bin/dex2oat --runtime-arg -classpath --runtime-arg /system/framework/XposedBridge.jar --instruction-set=arm --instruction-set-features=smp,-div,-atomic_ldrd_strd --runtime-arg -Xnorelocate --boot-image=/system/framework/boot.art --runtime-arg -Xms64m --runtime-arg -Xmx512m --instruction-set-variant=krait --instruction-set-features=default --dex-file=/data/data/com.google.android.gms/app_chimera/m/00000014/oat/arm/DynamiteModulesA_GmsCore_prodmnc_xhdpi_release.odex --oat-file=/data/dalvik-cache/arm/data@data@com.google.android.gms@app_chimera@m@00000014@DynamiteModulesA_GmsCore_prodmnc_xhdpi_release.apk@classes.dex) because non-0 exit status