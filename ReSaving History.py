def parse_training_output(output):
    lines = output.strip().split('\n')
    history = {'accuracy': [], 'val_accuracy': [], 'loss': [], 'val_loss': []}

    for line in lines:
        # Extract the values from each line
        parts = line.split(' - ')
        loss = float(parts[1].split(': ')[1])
        accuracy = float(parts[2].split(': ')[1])
        val_loss = float(parts[3].split(': ')[1])
        val_accuracy = float(parts[4].split(': ')[1])

        # Add the values to the history dictionary
        history['loss'].append(loss)
        history['accuracy'].append(accuracy)
        history['val_loss'].append(val_loss)
        history['val_accuracy'].append(val_accuracy)

    return history

# Your training data here (as a multiline string)
training_output = """Epoch 1/2001594/1594 [==============================] - 683s 428ms/step - loss: 0.5018 - accuracy: 0.4850 - val_loss: 0.4086 - val_accuracy: 0.5933
Epoch 2/200
1594/1594 [==============================] - 680s 427ms/step - loss: 0.4264 - accuracy: 0.5955 - val_loss: 0.3577 - val_accuracy: 0.7090
Epoch 3/200
1594/1594 [==============================] - 672s 421ms/step - loss: 0.4220 - accuracy: 0.5745 - val_loss: 0.3685 - val_accuracy: 0.7096
Epoch 4/200
1594/1594 [==============================] - 675s 424ms/step - loss: 0.4047 - accuracy: 0.5986 - val_loss: 0.3522 - val_accuracy: 0.7266
Epoch 5/200
1594/1594 [==============================] - 677s 425ms/step - loss: 0.4017 - accuracy: 0.6066 - val_loss: 0.3584 - val_accuracy: 0.6285
Epoch 6/200
1594/1594 [==============================] - 680s 426ms/step - loss: 0.3944 - accuracy: 0.6007 - val_loss: 0.3399 - val_accuracy: 0.7321
Epoch 7/200
1594/1594 [==============================] - 677s 425ms/step - loss: 0.3930 - accuracy: 0.5994 - val_loss: 0.3483 - val_accuracy: 0.6939
Epoch 8/200
1594/1594 [==============================] - 681s 428ms/step - loss: 0.3778 - accuracy: 0.6002 - val_loss: 0.3375 - val_accuracy: 0.7102
Epoch 9/200
1594/1594 [==============================] - 682s 428ms/step - loss: 0.3712 - accuracy: 0.6262 - val_loss: 0.3344 - val_accuracy: 0.7065
Epoch 10/200
1594/1594 [==============================] - 682s 428ms/step - loss: 0.3761 - accuracy: 0.6200 - val_loss: 0.3231 - val_accuracy: 0.6574
Epoch 11/200
1594/1594 [==============================] - 685s 430ms/step - loss: 0.3681 - accuracy: 0.6196 - val_loss: 0.3071 - val_accuracy: 0.7128
Epoch 12/200
1594/1594 [==============================] - 682s 428ms/step - loss: 0.3685 - accuracy: 0.6353 - val_loss: 0.3231 - val_accuracy: 0.7071
Epoch 13/200
1594/1594 [==============================] - 684s 429ms/step - loss: 0.3633 - accuracy: 0.6320 - val_loss: 0.3123 - val_accuracy: 0.7547
Epoch 14/200
1594/1594 [==============================] - 681s 427ms/step - loss: 0.3660 - accuracy: 0.6298 - val_loss: 0.3041 - val_accuracy: 0.7511
Epoch 15/200
1594/1594 [==============================] - 680s 427ms/step - loss: 0.3637 - accuracy: 0.6320 - val_loss: 0.3317 - val_accuracy: 0.7234
Epoch 16/200
1594/1594 [==============================] - 680s 427ms/step - loss: 0.3542 - accuracy: 0.6443 - val_loss: 0.3013 - val_accuracy: 0.7555
Epoch 17/200
1594/1594 [==============================] - 681s 427ms/step - loss: 0.3588 - accuracy: 0.6344 - val_loss: 0.3401 - val_accuracy: 0.6738
Epoch 18/200
1594/1594 [==============================] - 685s 429ms/step - loss: 0.3571 - accuracy: 0.6454 - val_loss: 0.2975 - val_accuracy: 0.7656
Epoch 19/200
1594/1594 [==============================] - 685s 430ms/step - loss: 0.3537 - accuracy: 0.6118 - val_loss: 0.3025 - val_accuracy: 0.7656
Epoch 20/200
1594/1594 [==============================] - 683s 429ms/step - loss: 0.3497 - accuracy: 0.6371 - val_loss: 0.3097 - val_accuracy: 0.7612
Epoch 21/200
1594/1594 [==============================] - 684s 429ms/step - loss: 0.3514 - accuracy: 0.6313 - val_loss: 0.3035 - val_accuracy: 0.7541
Epoch 22/200
1594/1594 [==============================] - 687s 431ms/step - loss: 0.3494 - accuracy: 0.6452 - val_loss: 0.3046 - val_accuracy: 0.7442
Epoch 23/200
1594/1594 [==============================] - 680s 427ms/step - loss: 0.3466 - accuracy: 0.6388 - val_loss: 0.3008 - val_accuracy: 0.7467
Epoch 24/200
1594/1594 [==============================] - 686s 430ms/step - loss: 0.3495 - accuracy: 0.6174 - val_loss: 0.2940 - val_accuracy: 0.7756
Epoch 25/200
1594/1594 [==============================] - 682s 428ms/step - loss: 0.3473 - accuracy: 0.6477 - val_loss: 0.2984 - val_accuracy: 0.7555
Epoch 26/200
1594/1594 [==============================] - 681s 427ms/step - loss: 0.3469 - accuracy: 0.6226 - val_loss: 0.3021 - val_accuracy: 0.7618
Epoch 27/200
1594/1594 [==============================] - 688s 431ms/step - loss: 0.3447 - accuracy: 0.6593 - val_loss: 0.3037 - val_accuracy: 0.7536
Epoch 28/200
1594/1594 [==============================] - 681s 427ms/step - loss: 0.3460 - accuracy: 0.6134 - val_loss: 0.2961 - val_accuracy: 0.7498
Epoch 29/200
1594/1594 [==============================] - 683s 429ms/step - loss: 0.3409 - accuracy: 0.6239 - val_loss: 0.2877 - val_accuracy: 0.7805
Epoch 30/200
1594/1594 [==============================] - 686s 431ms/step - loss: 0.3399 - accuracy: 0.6360 - val_loss: 0.3143 - val_accuracy: 0.7354
Epoch 31/200
1594/1594 [==============================] - 691s 434ms/step - loss: 0.3396 - accuracy: 0.6258 - val_loss: 0.2969 - val_accuracy: 0.7586
Epoch 32/200
1594/1594 [==============================] - 683s 429ms/step - loss: 0.3366 - accuracy: 0.6487 - val_loss: 0.2974 - val_accuracy: 0.7630
Epoch 33/200
1594/1594 [==============================] - 683s 428ms/step - loss: 0.3377 - accuracy: 0.6344 - val_loss: 0.3097 - val_accuracy: 0.7492
Epoch 34/200
1594/1594 [==============================] - 687s 431ms/step - loss: 0.3366 - accuracy: 0.6578 - val_loss: 0.3081 - val_accuracy: 0.7549
Epoch 35/200
1594/1594 [==============================] - 686s 430ms/step - loss: 0.3319 - accuracy: 0.6269 - val_loss: 0.2981 - val_accuracy: 0.7511
Epoch 36/200
1594/1594 [==============================] - 681s 427ms/step - loss: 0.3404 - accuracy: 0.6058 - val_loss: 0.2864 - val_accuracy: 0.7717
Epoch 37/200
1594/1594 [==============================] - 685s 430ms/step - loss: 0.3378 - accuracy: 0.6239 - val_loss: 0.2947 - val_accuracy: 0.7612
Epoch 38/200
1594/1594 [==============================] - 685s 430ms/step - loss: 0.3357 - accuracy: 0.6378 - val_loss: 0.3006 - val_accuracy: 0.7542
Epoch 39/200
1594/1594 [==============================] - 684s 429ms/step - loss: 0.3350 - accuracy: 0.6355 - val_loss: 0.2886 - val_accuracy: 0.7762
Epoch 40/200
1594/1594 [==============================] - 694s 435ms/step - loss: 0.3312 - accuracy: 0.6247 - val_loss: 0.2854 - val_accuracy: 0.7511
Epoch 41/200
1594/1594 [==============================] - 687s 431ms/step - loss: 0.3302 - accuracy: 0.6254 - val_loss: 0.2943 - val_accuracy: 0.7700
Epoch 42/200
1594/1594 [==============================] - 684s 429ms/step - loss: 0.3329 - accuracy: 0.6502 - val_loss: 0.2900 - val_accuracy: 0.7599
Epoch 43/200
1594/1594 [==============================] - 688s 432ms/step - loss: 0.3345 - accuracy: 0.6404 - val_loss: 0.2750 - val_accuracy: 0.6556
Epoch 44/200
1594/1594 [==============================] - 683s 429ms/step - loss: 0.3316 - accuracy: 0.6156 - val_loss: 0.3012 - val_accuracy: 0.7484
Epoch 45/200
1594/1594 [==============================] - 687s 431ms/step - loss: 0.3320 - accuracy: 0.6487 - val_loss: 0.2917 - val_accuracy: 0.7542
Epoch 46/200
1594/1594 [==============================] - 685s 430ms/step - loss: 0.3354 - accuracy: 0.6564 - val_loss: 0.2886 - val_accuracy: 0.7718
Epoch 47/200
1594/1594 [==============================] - 687s 431ms/step - loss: 0.3276 - accuracy: 0.6369 - val_loss: 0.2897 - val_accuracy: 0.7492
Epoch 48/200
1594/1594 [==============================] - 685s 430ms/step - loss: 0.3308 - accuracy: 0.6250 - val_loss: 0.2998 - val_accuracy: 0.7574
Epoch 49/200
1594/1594 [==============================] - 684s 429ms/step - loss: 0.3281 - accuracy: 0.6325 - val_loss: 0.2845 - val_accuracy: 0.7718
Epoch 50/200
1594/1594 [==============================] - 687s 431ms/step - loss: 0.3312 - accuracy: 0.6378 - val_loss: 0.2815 - val_accuracy: 0.7197
Epoch 51/200
1594/1594 [==============================] - 687s 431ms/step - loss: 0.3306 - accuracy: 0.6025 - val_loss: 0.2835 - val_accuracy: 0.7762
Epoch 52/200
1594/1594 [==============================] - 686s 430ms/step - loss: 0.3322 - accuracy: 0.6016 - val_loss: 0.2741 - val_accuracy: 0.6421
Epoch 53/200
1594/1594 [==============================] - 686s 430ms/step - loss: 0.3309 - accuracy: 0.6466 - val_loss: 0.2810 - val_accuracy: 0.7687
Epoch 54/200
1594/1594 [==============================] - 689s 432ms/step - loss: 0.3256 - accuracy: 0.6570 - val_loss: 0.2829 - val_accuracy: 0.7876
Epoch 55/200
1594/1594 [==============================] - 688s 432ms/step - loss: 0.3255 - accuracy: 0.6212 - val_loss: 0.2853 - val_accuracy: 0.7656
Epoch 56/200
1594/1594 [==============================] - 684s 429ms/step - loss: 0.3257 - accuracy: 0.6597 - val_loss: 0.2802 - val_accuracy: 0.7775
Epoch 57/200
1594/1594 [==============================] - 686s 430ms/step - loss: 0.3305 - accuracy: 0.6270 - val_loss: 0.3057 - val_accuracy: 0.7580
Epoch 58/200
1594/1594 [==============================] - 691s 433ms/step - loss: 0.3230 - accuracy: 0.6451 - val_loss: 0.2824 - val_accuracy: 0.7813
Epoch 59/200
1594/1594 [==============================] - 684s 429ms/step - loss: 0.3256 - accuracy: 0.6371 - val_loss: 0.2834 - val_accuracy: 0.6849
Epoch 60/200
1594/1594 [==============================] - 687s 431ms/step - loss: 0.3194 - accuracy: 0.6057 - val_loss: 0.2933 - val_accuracy: 0.7649
Epoch 61/200
1594/1594 [==============================] - 686s 430ms/step - loss: 0.3229 - accuracy: 0.6231 - val_loss: 0.2749 - val_accuracy: 0.5864
Epoch 62/200
1594/1594 [==============================] - 688s 432ms/step - loss: 0.3211 - accuracy: 0.6239 - val_loss: 0.2826 - val_accuracy: 0.7555
Epoch 63/200
1594/1594 [==============================] - 687s 431ms/step - loss: 0.3257 - accuracy: 0.6338 - val_loss: 0.2797 - val_accuracy: 0.7442
Epoch 64/200
1594/1594 [==============================] - 688s 432ms/step - loss: 0.3232 - accuracy: 0.6388 - val_loss: 0.3042 - val_accuracy: 0.6788
Epoch 65/200
1594/1594 [==============================] - 689s 433ms/step - loss: 0.3229 - accuracy: 0.6325 - val_loss: 0.2750 - val_accuracy: 0.6235
Epoch 66/200
1594/1594 [==============================] - 685s 430ms/step - loss: 0.3213 - accuracy: 0.6322 - val_loss: 0.2944 - val_accuracy: 0.7172
Epoch 67/200
1594/1594 [==============================] - 686s 430ms/step - loss: 0.3200 - accuracy: 0.6140 - val_loss: 0.2864 - val_accuracy: 0.5403
Epoch 68/200
1594/1594 [==============================] - 685s 430ms/step - loss: 0.3167 - accuracy: 0.6360 - val_loss: 0.2736 - val_accuracy: 0.7700
Epoch 69/200
1594/1594 [==============================] - 688s 432ms/step - loss: 0.3197 - accuracy: 0.6382 - val_loss: 0.2764 - val_accuracy: 0.7700
Epoch 70/200
1594/1594 [==============================] - 687s 431ms/step - loss: 0.3187 - accuracy: 0.6451 - val_loss: 0.2833 - val_accuracy: 0.7656
Epoch 71/200
1594/1594 [==============================] - 685s 430ms/step - loss: 0.3197 - accuracy: 0.6344 - val_loss: 0.2715 - val_accuracy: 0.7209
Epoch 72/200
1594/1594 [==============================] - 683s 428ms/step - loss: 0.3234 - accuracy: 0.6380 - val_loss: 0.3020 - val_accuracy: 0.7593
Epoch 73/200
1594/1594 [==============================] - 685s 430ms/step - loss: 0.3185 - accuracy: 0.6377 - val_loss: 0.2955 - val_accuracy: 0.7800
Epoch 74/200
1594/1594 [==============================] - 684s 429ms/step - loss: 0.3160 - accuracy: 0.6382 - val_loss: 0.2730 - val_accuracy: 0.7373
Epoch 75/200
1594/1594 [==============================] - 687s 431ms/step - loss: 0.3194 - accuracy: 0.6333 - val_loss: 0.2949 - val_accuracy: 0.7132
Epoch 76/200
1594/1594 [==============================] - 688s 431ms/step - loss: 0.3220 - accuracy: 0.5961 - val_loss: 0.2788 - val_accuracy: 0.5600
Epoch 77/200
1594/1594 [==============================] - 683s 428ms/step - loss: 0.3234 - accuracy: 0.6137 - val_loss: 0.2713 - val_accuracy: 0.7800
Epoch 78/200
1594/1594 [==============================] - 683s 428ms/step - loss: 0.3158 - accuracy: 0.6458 - val_loss: 0.2844 - val_accuracy: 0.7498
Epoch 79/200
1594/1594 [==============================] - 687s 431ms/step - loss: 0.3172 - accuracy: 0.6510 - val_loss: 0.2743 - val_accuracy: 0.7649
Epoch 80/200
1594/1594 [==============================] - 690s 433ms/step - loss: 0.3150 - accuracy: 0.6154 - val_loss: 0.2857 - val_accuracy: 0.6989
Epoch 81/200
1594/1594 [==============================] - 690s 433ms/step - loss: 0.3204 - accuracy: 0.6104 - val_loss: 0.2879 - val_accuracy: 0.7580
Epoch 82/200
1594/1594 [==============================] - 682s 428ms/step - loss: 0.3150 - accuracy: 0.6325 - val_loss: 0.2653 - val_accuracy: 0.7792
Epoch 83/200
1594/1594 [==============================] - 684s 429ms/step - loss: 0.3129 - accuracy: 0.6441 - val_loss: 0.2733 - val_accuracy: 0.7549
Epoch 84/200
1594/1594 [==============================] - 684s 429ms/step - loss: 0.3154 - accuracy: 0.6173 - val_loss: 0.2665 - val_accuracy: 0.7876
Epoch 85/200
1594/1594 [==============================] - 684s 429ms/step - loss: 0.3158 - accuracy: 0.6388 - val_loss: 0.2929 - val_accuracy: 0.7058
Epoch 86/200
1594/1594 [==============================] - 685s 430ms/step - loss: 0.3187 - accuracy: 0.6311 - val_loss: 0.2680 - val_accuracy: 0.8096
Epoch 87/200
1594/1594 [==============================] - 689s 433ms/step - loss: 0.3153 - accuracy: 0.6482 - val_loss: 0.2747 - val_accuracy: 0.6380
Epoch 88/200
1594/1594 [==============================] - 687s 431ms/step - loss: 0.3152 - accuracy: 0.6140 - val_loss: 0.3107 - val_accuracy: 0.6845
Epoch 89/200
1594/1594 [==============================] - 684s 429ms/step - loss: 0.3159 - accuracy: 0.6601 - val_loss: 0.2763 - val_accuracy: 0.7725
Epoch 90/200
1594/1594 [==============================] - 685s 430ms/step - loss: 0.3054 - accuracy: 0.6267 - val_loss: 0.2800 - val_accuracy: 0.7308
Epoch 91/200
1594/1594 [==============================] - 684s 429ms/step - loss: 0.3176 - accuracy: 0.6419 - val_loss: 0.2697 - val_accuracy: 0.7838
Epoch 92/200
1594/1594 [==============================] - 686s 431ms/step - loss: 0.3161 - accuracy: 0.6424 - val_loss: 0.2726 - val_accuracy: 0.7832
Epoch 93/200
1594/1594 [==============================] - 693s 435ms/step - loss: 0.3111 - accuracy: 0.6382 - val_loss: 0.2809 - val_accuracy: 0.7819
Epoch 94/200
1594/1594 [==============================] - 685s 430ms/step - loss: 0.3164 - accuracy: 0.6273 - val_loss: 0.2720 - val_accuracy: 0.5933
Epoch 95/200
1594/1594 [==============================] - 691s 434ms/step - loss: 0.3119 - accuracy: 0.6116 - val_loss: 0.2863 - val_accuracy: 0.5223
Epoch 96/200
1594/1594 [==============================] - 684s 429ms/step - loss: 0.3123 - accuracy: 0.6466 - val_loss: 0.2670 - val_accuracy: 0.7498
Epoch 97/200
1594/1594 [==============================] - 687s 431ms/step - loss: 0.3098 - accuracy: 0.6206 - val_loss: 0.2852 - val_accuracy: 0.7712
Epoch 98/200
1594/1594 [==============================] - 684s 429ms/step - loss: 0.3177 - accuracy: 0.6308 - val_loss: 0.2712 - val_accuracy: 0.6767
Epoch 99/200
1594/1594 [==============================] - 684s 429ms/step - loss: 0.3138 - accuracy: 0.6196 - val_loss: 0.2770 - val_accuracy: 0.7769
Epoch 100/200
1594/1594 [==============================] - 686s 431ms/step - loss: 0.3097 - accuracy: 0.6549 - val_loss: 0.2798 - val_accuracy: 0.7605
Epoch 101/200
1594/1594 [==============================] - 702s 441ms/step - loss: 0.3144 - accuracy: 0.6435 - val_loss: 0.2846 - val_accuracy: 0.7310
Epoch 102/200
1594/1594 [==============================] - 711s 446ms/step - loss: 0.3083 - accuracy: 0.6291 - val_loss: 0.2708 - val_accuracy: 0.7869
Epoch 103/200
1594/1594 [==============================] - 718s 451ms/step - loss: 0.3148 - accuracy: 0.6432 - val_loss: 0.2692 - val_accuracy: 0.7806
Epoch 104/200
1594/1594 [==============================] - 715s 449ms/step - loss: 0.3110 - accuracy: 0.6123 - val_loss: 0.2708 - val_accuracy: 0.7360
Epoch 105/200
1594/1594 [==============================] - 716s 449ms/step - loss: 0.3108 - accuracy: 0.6338 - val_loss: 0.2682 - val_accuracy: 0.6660
Epoch 106/200
1594/1594 [==============================] - 714s 448ms/step - loss: 0.3144 - accuracy: 0.6322 - val_loss: 0.2655 - val_accuracy: 0.5757
Epoch 107/200
1594/1594 [==============================] - 719s 451ms/step - loss: 0.3058 - accuracy: 0.6185 - val_loss: 0.2809 - val_accuracy: 0.7775
Epoch 108/200
1594/1594 [==============================] - 714s 448ms/step - loss: 0.3074 - accuracy: 0.6458 - val_loss: 0.2779 - val_accuracy: 0.6430
Epoch 109/200
1594/1594 [==============================] - 713s 448ms/step - loss: 0.3080 - accuracy: 0.6157 - val_loss: 0.2899 - val_accuracy: 0.7109
Epoch 110/200
1594/1594 [==============================] - 709s 445ms/step - loss: 0.3086 - accuracy: 0.6367 - val_loss: 0.2739 - val_accuracy: 0.7568
Epoch 111/200
1594/1594 [==============================] - 705s 442ms/step - loss: 0.3103 - accuracy: 0.6429 - val_loss: 0.2728 - val_accuracy: 0.7888
Epoch 112/200
1594/1594 [==============================] - 698s 438ms/step - loss: 0.3132 - accuracy: 0.6289 - val_loss: 0.2722 - val_accuracy: 0.7656
Epoch 113/200
1594/1594 [==============================] - 704s 442ms/step - loss: 0.3065 - accuracy: 0.6495 - val_loss: 0.2653 - val_accuracy: 0.7824
Epoch 114/200
1594/1594 [==============================] - 703s 441ms/step - loss: 0.3080 - accuracy: 0.6393 - val_loss: 0.2749 - val_accuracy: 0.7819
Epoch 115/200
1594/1594 [==============================] - 705s 442ms/step - loss: 0.3148 - accuracy: 0.6297 - val_loss: 0.2659 - val_accuracy: 0.7945
Epoch 116/200
1594/1594 [==============================] - 706s 443ms/step - loss: 0.3084 - accuracy: 0.6295 - val_loss: 0.2717 - val_accuracy: 0.7291
Epoch 117/200
1594/1594 [==============================] - 711s 446ms/step - loss: 0.3092 - accuracy: 0.6355 - val_loss: 0.2686 - val_accuracy: 0.7467
Epoch 118/200
1594/1594 [==============================] - 711s 446ms/step - loss: 0.3102 - accuracy: 0.6355 - val_loss: 0.2799 - val_accuracy: 0.6329
Epoch 119/200
1594/1594 [==============================] - 704s 442ms/step - loss: 0.3049 - accuracy: 0.6306 - val_loss: 0.2775 - val_accuracy: 0.7046
Epoch 120/200
1594/1594 [==============================] - 717s 450ms/step - loss: 0.3082 - accuracy: 0.6460 - val_loss: 0.2700 - val_accuracy: 0.7976
Epoch 121/200
1594/1594 [==============================] - 705s 442ms/step - loss: 0.3038 - accuracy: 0.6104 - val_loss: 0.2628 - val_accuracy: 0.6233
Epoch 122/200
1594/1594 [==============================] - 704s 442ms/step - loss: 0.3056 - accuracy: 0.6245 - val_loss: 0.2645 - val_accuracy: 0.6631
Epoch 123/200
1594/1594 [==============================] - 712s 447ms/step - loss: 0.3054 - accuracy: 0.6415 - val_loss: 0.2760 - val_accuracy: 0.7511
Epoch 124/200
1594/1594 [==============================] - 755s 474ms/step - loss: 0.3084 - accuracy: 0.6314 - val_loss: 0.2802 - val_accuracy: 0.7599
Epoch 125/200
1594/1594 [==============================] - 714s 448ms/step - loss: 0.3052 - accuracy: 0.6201 - val_loss: 0.2631 - val_accuracy: 0.6348
Epoch 126/200
1594/1594 [==============================] - 696s 437ms/step - loss: 0.3116 - accuracy: 0.6138 - val_loss: 0.2675 - val_accuracy: 0.7762
Epoch 127/200
1594/1594 [==============================] - 701s 440ms/step - loss: 0.3047 - accuracy: 0.6204 - val_loss: 0.2921 - val_accuracy: 0.7568
Epoch 128/200
1594/1594 [==============================] - 715s 449ms/step - loss: 0.3062 - accuracy: 0.6182 - val_loss: 0.2836 - val_accuracy: 0.7434
Epoch 129/200
1594/1594 [==============================] - 701s 440ms/step - loss: 0.3146 - accuracy: 0.6104 - val_loss: 0.2685 - val_accuracy: 0.7542
Epoch 130/200
1594/1594 [==============================] - 709s 445ms/step - loss: 0.3042 - accuracy: 0.6255 - val_loss: 0.2770 - val_accuracy: 0.7731
Epoch 131/200
1594/1594 [==============================] - 706s 443ms/step - loss: 0.3027 - accuracy: 0.6361 - val_loss: 0.2548 - val_accuracy: 0.7725
Epoch 132/200
1594/1594 [==============================] - 706s 443ms/step - loss: 0.3079 - accuracy: 0.6273 - val_loss: 0.2667 - val_accuracy: 0.7172
Epoch 133/200
1594/1594 [==============================] - 705s 443ms/step - loss: 0.3042 - accuracy: 0.6421 - val_loss: 0.2785 - val_accuracy: 0.6675
Epoch 134/200
1594/1594 [==============================] - 706s 443ms/step - loss: 0.3100 - accuracy: 0.6121 - val_loss: 0.2619 - val_accuracy: 0.6323
Epoch 135/200
1594/1594 [==============================] - 698s 438ms/step - loss: 0.3008 - accuracy: 0.6062 - val_loss: 0.2705 - val_accuracy: 0.6700
Epoch 136/200
1594/1594 [==============================] - 706s 443ms/step - loss: 0.3101 - accuracy: 0.6515 - val_loss: 0.2665 - val_accuracy: 0.6774
Epoch 137/200
1594/1594 [==============================] - 700s 439ms/step - loss: 0.3086 - accuracy: 0.6058 - val_loss: 0.2989 - val_accuracy: 0.6939
Epoch 138/200
1594/1594 [==============================] - 711s 446ms/step - loss: 0.3024 - accuracy: 0.6090 - val_loss: 0.2668 - val_accuracy: 0.7329
Epoch 139/200
1594/1594 [==============================] - 715s 449ms/step - loss: 0.3019 - accuracy: 0.6422 - val_loss: 0.2765 - val_accuracy: 0.7429
Epoch 140/200
1594/1594 [==============================] - 702s 441ms/step - loss: 0.3059 - accuracy: 0.6062 - val_loss: 0.2816 - val_accuracy: 0.6562
Epoch 141/200
1594/1594 [==============================] - 704s 442ms/step - loss: 0.3053 - accuracy: 0.6167 - val_loss: 0.2611 - val_accuracy: 0.7241
Epoch 142/200
1594/1594 [==============================] - 711s 446ms/step - loss: 0.3021 - accuracy: 0.6149 - val_loss: 0.2653 - val_accuracy: 0.7517
Epoch 143/200
1594/1594 [==============================] - 714s 448ms/step - loss: 0.3054 - accuracy: 0.6229 - val_loss: 0.2735 - val_accuracy: 0.6769
Epoch 144/200
1594/1594 [==============================] - 711s 446ms/step - loss: 0.3042 - accuracy: 0.6204 - val_loss: 0.2946 - val_accuracy: 0.7516
Epoch 145/200
1594/1594 [==============================] - 701s 440ms/step - loss: 0.3003 - accuracy: 0.6393 - val_loss: 0.2707 - val_accuracy: 0.6562
Epoch 146/200
1594/1594 [==============================] - 717s 450ms/step - loss: 0.3058 - accuracy: 0.6220 - val_loss: 0.2746 - val_accuracy: 0.7819
Epoch 147/200
1594/1594 [==============================] - 700s 440ms/step - loss: 0.3044 - accuracy: 0.6358 - val_loss: 0.2831 - val_accuracy: 0.7637
Epoch 148/200
1594/1594 [==============================] - 707s 444ms/step - loss: 0.3003 - accuracy: 0.6382 - val_loss: 0.2562 - val_accuracy: 0.7901
Epoch 149/200
1594/1594 [==============================] - 699s 439ms/step - loss: 0.3028 - accuracy: 0.6501 - val_loss: 0.2676 - val_accuracy: 0.7888
Epoch 150/200
1594/1594 [==============================] - 701s 440ms/step - loss: 0.3024 - accuracy: 0.6529 - val_loss: 0.2689 - val_accuracy: 0.7649
Epoch 151/200
1594/1594 [==============================] - 703s 441ms/step - loss: 0.3054 - accuracy: 0.6179 - val_loss: 0.2703 - val_accuracy: 0.7560
Epoch 152/200
1594/1594 [==============================] - 702s 440ms/step - loss: 0.2994 - accuracy: 0.6149 - val_loss: 0.2557 - val_accuracy: 0.6568
Epoch 153/200
1594/1594 [==============================] - 710s 445ms/step - loss: 0.3039 - accuracy: 0.6358 - val_loss: 0.2686 - val_accuracy: 0.7536
Epoch 154/200
1594/1594 [==============================] - 702s 440ms/step - loss: 0.2993 - accuracy: 0.6231 - val_loss: 0.2761 - val_accuracy: 0.7769
Epoch 155/200
1594/1594 [==============================] - 715s 448ms/step - loss: 0.2993 - accuracy: 0.6102 - val_loss: 0.2987 - val_accuracy: 0.6292
Epoch 156/200
1594/1594 [==============================] - 699s 439ms/step - loss: 0.3000 - accuracy: 0.6079 - val_loss: 0.2734 - val_accuracy: 0.5889
Epoch 157/200
1594/1594 [==============================] - 689s 433ms/step - loss: 0.2988 - accuracy: 0.6157 - val_loss: 0.2621 - val_accuracy: 0.7366
Epoch 158/200
1594/1594 [==============================] - 683s 429ms/step - loss: 0.3010 - accuracy: 0.6124 - val_loss: 0.2583 - val_accuracy: 0.7674
Epoch 159/200
1594/1594 [==============================] - 695s 436ms/step - loss: 0.2956 - accuracy: 0.6311 - val_loss: 0.2830 - val_accuracy: 0.6371
Epoch 160/200
1594/1594 [==============================] - 699s 438ms/step - loss: 0.3013 - accuracy: 0.6250 - val_loss: 0.2599 - val_accuracy: 0.7901
Epoch 161/200
1594/1594 [==============================] - 693s 435ms/step - loss: 0.3041 - accuracy: 0.6077 - val_loss: 0.2763 - val_accuracy: 0.7800
Epoch 162/200
1594/1594 [==============================] - 689s 432ms/step - loss: 0.3040 - accuracy: 0.6488 - val_loss: 0.2735 - val_accuracy: 0.7366
Epoch 163/200
1594/1594 [==============================] - 692s 434ms/step - loss: 0.2964 - accuracy: 0.6120 - val_loss: 0.2825 - val_accuracy: 0.5405
Epoch 164/200
1594/1594 [==============================] - 687s 431ms/step - loss: 0.3015 - accuracy: 0.6104 - val_loss: 0.2602 - val_accuracy: 0.7291
Epoch 165/200
1594/1594 [==============================] - 691s 434ms/step - loss: 0.3056 - accuracy: 0.6118 - val_loss: 0.2617 - val_accuracy: 0.5959
Epoch 166/200
1594/1594 [==============================] - 689s 432ms/step - loss: 0.3012 - accuracy: 0.6248 - val_loss: 0.2776 - val_accuracy: 0.5739
Epoch 167/200
1594/1594 [==============================] - 690s 433ms/step - loss: 0.3006 - accuracy: 0.6256 - val_loss: 0.2614 - val_accuracy: 0.7283
Epoch 168/200
1594/1594 [==============================] - 690s 433ms/step - loss: 0.2983 - accuracy: 0.6062 - val_loss: 0.2783 - val_accuracy: 0.7549
Epoch 169/200
1594/1594 [==============================] - 702s 440ms/step - loss: 0.2986 - accuracy: 0.6134 - val_loss: 0.2676 - val_accuracy: 0.6952
Epoch 170/200
1594/1594 [==============================] - 691s 434ms/step - loss: 0.3066 - accuracy: 0.6126 - val_loss: 0.2640 - val_accuracy: 0.5896
Epoch 171/200
1594/1594 [==============================] - 694s 435ms/step - loss: 0.2954 - accuracy: 0.6394 - val_loss: 0.2742 - val_accuracy: 0.6788
Epoch 172/200
1594/1594 [==============================] - 696s 437ms/step - loss: 0.3020 - accuracy: 0.6090 - val_loss: 0.2529 - val_accuracy: 0.5820
Epoch 173/200
1594/1594 [==============================] - 689s 433ms/step - loss: 0.2981 - accuracy: 0.6421 - val_loss: 0.2702 - val_accuracy: 0.7291
Epoch 174/200
1594/1594 [==============================] - 689s 432ms/step - loss: 0.2950 - accuracy: 0.6341 - val_loss: 0.2632 - val_accuracy: 0.7509
Epoch 175/200
1594/1594 [==============================] - 692s 434ms/step - loss: 0.2989 - accuracy: 0.6325 - val_loss: 0.2591 - val_accuracy: 0.6361
Epoch 176/200
1594/1594 [==============================] - 688s 432ms/step - loss: 0.3062 - accuracy: 0.6546 - val_loss: 0.2719 - val_accuracy: 0.7850
Epoch 177/200
1594/1594 [==============================] - 691s 434ms/step - loss: 0.3006 - accuracy: 0.6096 - val_loss: 0.2658 - val_accuracy: 0.7209
Epoch 178/200
1594/1594 [==============================] - 692s 434ms/step - loss: 0.2986 - accuracy: 0.6244 - val_loss: 0.2622 - val_accuracy: 0.7561
Epoch 179/200
1594/1594 [==============================] - 690s 433ms/step - loss: 0.3019 - accuracy: 0.6341 - val_loss: 0.2710 - val_accuracy: 0.7618
Epoch 180/200
1594/1594 [==============================] - 689s 433ms/step - loss: 0.3021 - accuracy: 0.6295 - val_loss: 0.2640 - val_accuracy: 0.7046
Epoch 181/200
1594/1594 [==============================] - 691s 434ms/step - loss: 0.2951 - accuracy: 0.6317 - val_loss: 0.2615 - val_accuracy: 0.7398
Epoch 182/200
1594/1594 [==============================] - 690s 433ms/step - loss: 0.2996 - accuracy: 0.6377 - val_loss: 0.2740 - val_accuracy: 0.7591
Epoch 183/200
1594/1594 [==============================] - 699s 439ms/step - loss: 0.3005 - accuracy: 0.6446 - val_loss: 0.2871 - val_accuracy: 0.7649
Epoch 184/200
1594/1594 [==============================] - 692s 434ms/step - loss: 0.3053 - accuracy: 0.6319 - val_loss: 0.2560 - val_accuracy: 0.6518
Epoch 185/200
1594/1594 [==============================] - 690s 433ms/step - loss: 0.2991 - accuracy: 0.6280 - val_loss: 0.2639 - val_accuracy: 0.7825
Epoch 186/200
1594/1594 [==============================] - 690s 433ms/step - loss: 0.3014 - accuracy: 0.6582 - val_loss: 0.2769 - val_accuracy: 0.6021
Epoch 187/200
1594/1594 [==============================] - 690s 433ms/step - loss: 0.3034 - accuracy: 0.6036 - val_loss: 0.2746 - val_accuracy: 0.7674
Epoch 188/200
1594/1594 [==============================] - 691s 433ms/step - loss: 0.3019 - accuracy: 0.6302 - val_loss: 0.2583 - val_accuracy: 0.5940
Epoch 189/200
1594/1594 [==============================] - 690s 433ms/step - loss: 0.2979 - accuracy: 0.6366 - val_loss: 0.2714 - val_accuracy: 0.7769
Epoch 190/200
1594/1594 [==============================] - 691s 434ms/step - loss: 0.2990 - accuracy: 0.6298 - val_loss: 0.2587 - val_accuracy: 0.6107
Epoch 191/200
1594/1594 [==============================] - 691s 433ms/step - loss: 0.2957 - accuracy: 0.6105 - val_loss: 0.2629 - val_accuracy: 0.7863
Epoch 192/200
1594/1594 [==============================] - 694s 435ms/step - loss: 0.2980 - accuracy: 0.6344 - val_loss: 0.2688 - val_accuracy: 0.7354
Epoch 193/200
1594/1594 [==============================] - 691s 434ms/step - loss: 0.2931 - accuracy: 0.6055 - val_loss: 0.2734 - val_accuracy: 0.7184
Epoch 194/200
1594/1594 [==============================] - 688s 432ms/step - loss: 0.3064 - accuracy: 0.6413 - val_loss: 0.2572 - val_accuracy: 0.7568
Epoch 195/200
1594/1594 [==============================] - 687s 431ms/step - loss: 0.2999 - accuracy: 0.6231 - val_loss: 0.2708 - val_accuracy: 0.6882
Epoch 196/200
1594/1594 [==============================] - 689s 433ms/step - loss: 0.3001 - accuracy: 0.6102 - val_loss: 0.2658 - val_accuracy: 0.7926
Epoch 197/200
1594/1594 [==============================] - 690s 433ms/step - loss: 0.2995 - accuracy: 0.6363 - val_loss: 0.2622 - val_accuracy: 0.7509
Epoch 198/200
1594/1594 [==============================] - 692s 434ms/step - loss: 0.2948 - accuracy: 0.6226 - val_loss: 0.2732 - val_accuracy: 0.7731
Epoch 199/200
1594/1594 [==============================] - 687s 431ms/step - loss: 0.2948 - accuracy: 0.5985 - val_loss: 0.2580 - val_accuracy: 0.6354
Epoch 200/200
1594/1594 [==============================] - 688s 432ms/step - loss: 0.3043 - accuracy: 0.6104 - val_loss: 0.2594 - val_accuracy: 0.8020
"""

# Parse the output and get the history
history = parse_training_output(training_output)

# Now you can use the history dictionary for plotting or analysis
