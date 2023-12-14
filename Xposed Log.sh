11-17 17:29:31.706 I/Xposed  (18973): -----------------
11-17 17:29:31.706 I/Xposed  (18973): Starting Xposed version 86, compiled for SDK 23
11-17 17:29:31.706 I/Xposed  (18973): Device: Nexus 7 (asus), Android version 6.0.1 (SDK 23)
11-17 17:29:31.706 I/Xposed  (18973): ROM: cm_deb-userdebug 6.0.1 MOB31K 4fbf2568fa test-keys
11-17 17:29:31.706 I/Xposed  (18973): Build fingerprint: google/razorg/deb:6.0.1/MOB30X/3036618:user/release-keys
11-17 17:29:31.706 I/Xposed  (18973): Platform: armeabi-v7a, 32-bit binary, system server: yes
11-17 17:29:31.706 I/Xposed  (18973): SELinux enabled: yes, enforcing: yes
11-17 17:29:31.717 I/Xposed  (18973): -----------------
11-17 17:29:31.717 I/Xposed  (18973): Added Xposed (/system/framework/XposedBridge.jar) to CLASSPATH
11-17 17:29:31.871 I/Xposed  (18973): Detected ART runtime
11-17 17:29:31.875 I/Xposed  (18973): Found Xposed class 'de/robv/android/xposed/XposedBridge', now initializing
11-17 17:29:32.031 I/Xposed  (18973): Loading modules from /data/app/ma.wanam.youtubeadaway-1/base.apk
11-17 17:29:32.144 I/Xposed  (18973):   Loading class ma.wanam.youtubeadaway.Xposed
11-17 17:29:33.688 F/art     (18973): art/runtime/jni_internal.cc:497] JNI FatalError called: frameworks/base/core/jni/com_android_internal_os_Zygote.cpp:478: Unable to construct file descriptor table.
11-17 17:29:33.730 F/art     (18973): art/runtime/runtime.cc:372] Runtime aborting...
11-17 17:29:33.730 F/art     (18973): art/runtime/runtime.cc:372] Aborting thread:
11-17 17:29:33.730 F/art     (18973): art/runtime/runtime.cc:372] "main" prio=5 tid=1 Native
11-17 17:29:33.730 F/art     (18973): art/runtime/runtime.cc:372]   | group="" sCount=0 dsCount=0 obj=0x74c315b8 self=0xb4ff6500
11-17 17:29:33.730 F/art     (18973): art/runtime/runtime.cc:372]   | sysTid=18973 nice=0 cgrp=default sched=0/0 handle=0xb6fb5b44
11-17 17:29:33.730 F/art     (18973): art/runtime/runtime.cc:372]   | state=R schedstat=( 0 0 0 ) utm=219 stm=32 core=1 HZ=100
11-17 17:29:33.730 F/art     (18973): art/runtime/runtime.cc:372]   | stack=0xbe16b000-0xbe16d000 stackSize=8MB
11-17 17:29:33.730 F/art     (18973): art/runtime/runtime.cc:372]   | held mutexes= "abort lock"
11-17 17:29:33.730 F/art     (18973): art/runtime/runtime.cc:372]   native: #00 pc 00350651  /system/lib/libart.so (_ZN3art15DumpNativeStackERNSt3__113basic_ostreamIcNS0_11char_traitsIcEEEEiPKcPNS_9ArtMethodEPv+116)
11-17 17:29:33.730 F/art     (18973): art/runtime/runtime.cc:372]   native: #01 pc 00331bfb  /system/lib/libart.so (_ZNK3art6Thread4DumpERNSt3__113basic_ostreamIcNS1_11char_traitsIcEEEE+138)
11-17 17:29:33.730 F/art     (18973): art/runtime/runtime.cc:372]   native: #02 pc 00315c4d  /system/lib/libart.so (_ZNK3art10AbortState10DumpThreadERNSt3__113basic_ostreamIcNS1_11char_traitsIcEEEEPNS_6ThreadE+20)
11-17 17:29:33.730 F/art     (18973): art/runtime/runtime.cc:372]   native: #03 pc 00315ec1  /system/lib/libart.so (_ZN3art7Runtime5AbortEv+532)
11-17 17:29:33.730 F/art     (18973): art/runtime/runtime.cc:372]   native: #04 pc 000f3bed  /system/lib/libart.so (_ZN3art10LogMessageD2Ev+1296)
11-17 17:29:33.730 F/art     (18973): art/runtime/runtime.cc:372]   native: #05 pc 0025e1a7  /system/lib/libart.so (_ZN3art3JNI10FatalErrorEP7_JNIEnvPKc+66)
11-17 17:29:33.730 F/art     (18973): art/runtime/runtime.cc:372]   native: #06 pc 000b59ef  /system/lib/libandroid_runtime.so (???)
11-17 17:29:33.730 F/art     (18973): art/runtime/runtime.cc:372]   native: #07 pc 000b5b05  /system/lib/libandroid_runtime.so (???)
11-17 17:29:33.730 F/art     (18973): art/runtime/runtime.cc:372]   native: #08 pc 000b6603  /system/lib/libandroid_runtime.so (???)
11-17 17:29:33.730 F/art     (18973): art/runtime/runtime.cc:372]   native: #09 pc 013a6557  /data/dalvik-cache/arm/system@framework@boot.oat (???)
11-17 17:29:33.730 F/art     (18973): art/runtime/runtime.cc:372]   at com.android.internal.os.Zygote.nativeForkSystemServer(Native method)
11-17 17:29:33.730 F/art     (18973): art/runtime/runtime.cc:372]   at com.android.internal.os.Zygote.forkSystemServer(Zygote.java:137)
11-17 17:29:33.730 F/art     (18973): art/runtime/runtime.cc:372]   at com.android.internal.os.ZygoteInit.startSystemServer(ZygoteInit.java:528)
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372]   at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:608)
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372]   at de.robv.android.xposed.XposedBridge.main(XposedBridge.java:102)
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372] Dumping all threads without appropriate locks held: thread list lock mutator lock
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372] All threads:
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372] DALVIK THREADS (1):
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372] "main" prio=5 tid=1 Runnable
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372]   | group="" sCount=0 dsCount=0 obj=0x74c315b8 self=0xb4ff6500
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372]   | sysTid=18973 nice=0 cgrp=default sched=0/0 handle=0xb6fb5b44
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372]   | state=R schedstat=( 0 0 0 ) utm=219 stm=34 core=1 HZ=100
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372]   | stack=0xbe16b000-0xbe16d000 stackSize=8MB
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372]   | held mutexes= "abort lock" "mutator lock"(shared held)
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372]   native: #00 pc 00350651  /system/lib/libart.so (_ZN3art15DumpNativeStackERNSt3__113basic_ostreamIcNS0_11char_traitsIcEEEEiPKcPNS_9ArtMethodEPv+116)
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372]   native: #01 pc 00331bfb  /system/lib/libart.so (_ZNK3art6Thread4DumpERNSt3__113basic_ostreamIcNS1_11char_traitsIcEEEE+138)
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372]   native: #02 pc 0033b209  /system/lib/libart.so (_ZN3art14DumpCheckpoint3RunEPNS_6ThreadE+420)
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372]   native: #03 pc 0033bd65  /system/lib/libart.so (_ZN3art10ThreadList13RunCheckpointEPNS_7ClosureE+192)
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372]   native: #04 pc 0033c265  /system/lib/libart.so (_ZN3art10ThreadList4DumpERNSt3__113basic_ostreamIcNS1_11char_traitsIcEEEE+124)
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372]   native: #05 pc 00315e43  /system/lib/libart.so (_ZN3art7Runtime5AbortEv+406)
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372]   native: #06 pc 000f3bed  /system/lib/libart.so (_ZN3art10LogMessageD2Ev+1296)
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372]   native: #07 pc 0025e1a7  /system/lib/libart.so (_ZN3art3JNI10FatalErrorEP7_JNIEnvPKc+66)
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372]   native: #08 pc 000b59ef  /system/lib/libandroid_runtime.so (???)
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372]   native: #09 pc 000b5b05  /system/lib/libandroid_runtime.so (???)
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372]   native: #10 pc 000b6603  /system/lib/libandroid_runtime.so (???)
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372]   native: #11 pc 013a6557  /data/dalvik-cache/arm/system@framework@boot.oat (Java_com_android_internal_os_Zygote_nativeForkSystemServer__II_3II_3_3IJJ+186)
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372]   at com.android.internal.os.Zygote.nativeForkSystemServer(Native method)
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372]   at com.android.internal.os.Zygote.forkSystemServer(Zygote.java:137)
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372]   at com.android.internal.os.ZygoteInit.startSystemServer(ZygoteInit.java:528)
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372]   at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:608)
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372]   at de.robv.android.xposed.XposedBridge.main(XposedBridge.java:102)
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372] 
11-17 17:29:33.731 F/art     (18973): art/runtime/runtime.cc:372]