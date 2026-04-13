"""
Implementation of a fractal dimension Extractor

Fractals: These are infinitely complex patterns that are self-similar across different scales.

- They help to place infinite dimensions inside a single dimension which can be helpful in high 
ordered dimension representation.
- Here the data is treated ad a cloud in space and we measure how it scales as we change 
resolution
"""

import numpy as np

def fractal_dimension(Z, threshold=0.5):
    """
    Calculates the Minkowski-Bouligand (Box-Counting) Dimension.

    Parameters
    ----------
    Z : 2D numpy array
        DESCRIPTION: A feature map or binary image.
    threshold : TYPE, optional
        DESCRIPTION. value to binarize the data.

    Returns
    -------
    None.

    """
    # Only count non-empty pixels
    Z = (Z > threshold)
    
    # Transform Z into a square matrix with side length as a power of 2
    p = min(Z.shape)
    n = 2**np.float64(np.log2(p))
    Z = Z[:int(n), :int(n)]
    
    # List of box sizes (powers of 2)
    scales = np.logspace(1, int(np.log2(n)), num=10, endpoint=False, base=2).astype(int)
    counts = []
    
    for size in scales:
        # reshape into blocks and check which blocks contain "data"
        # below is the block counting step
        count = 0
        for i in range(0, Z.shape[0], size):
            for j in range(0, Z.shape[1], size):
                if np.any(Z[i:i+size, j:j+size]):
                    count += 1
        counts.append(count)
        
        # perform a linear fit on the log-log plot
        # The slope of this line is the Fractal Dimension (D)
        
        coeffs = np.polyfit(np.log(scales), np.log(counts), 1)
        return -coeffs[0]
    
# Examplr usage:
dummy_data = np.random.rand(512, 512)
d = fractal_dimension(dummy_data)
print(f"Fractal Dimension: {d:.4f}")
        
        
        
        
        
        
        
        
        
        
        
        
        
        






























