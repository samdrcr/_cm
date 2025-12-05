#范權榮 111210557

import cmath

def dft(f):
    N = len(f)
    F = []
    
    for k in range(N):
        F_k = 0
        for n in range(N):
            exponent = -2j * cmath.pi * k * n / N
            F_k += f[n] * cmath.exp(exponent)
            
        F.append(F_k)
        
    return F
#范權榮 111210557
def idft(F):
    N = len(F)
    f = []
    
    for n in range(N):
        f_n = 0
        for k in range(N):
            exponent = 2j * cmath.pi * k * n / N
            f_n += F[k] * cmath.exp(exponent)
            
        f_n /= N
        f.append(f_n)
        
    return f
#范權榮 111210557
def verify_transformations(f_original):
    
    print(f"Original Signal (f): {f_original}")
#范權榮 111210557
    F_spectrum = dft(f_original)
    print("\nSpectrum (DFT(f)):")
    for i, val in enumerate(F_spectrum):
        print(f"  F[{i}] = {round(val.real, 4)} + {round(val.imag, 4)}j")
        
    f_reconstructed = idft(F_spectrum)
    print("\nReconstructed Signal (IDFT(F)):")
    
    is_match = True
    for i in range(len(f_original)):
        original = f_original[i]
        reconstructed_value = f_reconstructed[i]
        reconstructed_real = round(reconstructed_value.real, 8) 
        
        print(f"  f_original[{i}]: {original} | f_reconstructed[{i}]: {reconstructed_real}")
        
        if abs(original - reconstructed_real) > 1e-6:
            is_match = False

    return is_match
#范權榮 111210557
# --- MAIN EXECUTION ---
#范權榮 111210557
if __name__ == "__main__":
    # Define a simple example signal
    example_signal = [1.0, 0.0, 0.0, 0.0]
    
    print("--- Starting DFT/IDFT Verification ---")
    
    success = verify_transformations(example_signal)
#范權榮 111210557
    print("\n" + "="*50)
    if success:
        print("✅ VERIFICATION SUCCESSFUL: IDFT(DFT(f)) successfully reconstructed the original signal.")
    else:
        print("❌ VERIFICATION FAILED: The reconstructed signal does not match the original.")
    print("="*50)
    #范權榮 111210557
    #范權榮 111210557
    #范權榮 111210557
    #范權榮 111210557
    #范權榮 111210557