// DOM Elements
const form = document.getElementById('form');
const loading = document.getElementById('loading');
const result = document.getElementById('result');
const btn = document.getElementById('btn');

/**
 * Load fraud example data into the form
 */
function loadFraud() {
    document.getElementById('Time').value = 406;
    document.getElementById('Amount').value = 245.67;
    document.getElementById('V1').value = -1.36;
    document.getElementById('V2').value = -0.07;
    document.getElementById('V3').value = 2.54;
    document.getElementById('V4').value = 1.38;
}

/**
 * Load legitimate transaction example data into the form
 */
function loadLegit() {
    document.getElementById('Time').value = 0;
    document.getElementById('Amount').value = 149.62;
    document.getElementById('V1').value = 1.19;
    document.getElementById('V2').value = 0.27;
    document.getElementById('V3').value = 0.17;
    document.getElementById('V4').value = 0.45;
}

/**
 * Clear the form and hide results
 */
function clearForm() {
    form.reset();
    result.style.display = 'none';
}

/**
 * Collect all feature values from the form
 * @returns {Object} Features object with all input values
 */
function collectFeatures() {
    const features = {
        Time: parseFloat(document.getElementById('Time').value) || 0,
        Amount: parseFloat(document.getElementById('Amount').value) || 0
    };

    // Collect V1-V28 features
    for (let i = 1; i <= 28; i++) {
        features[`V${i}`] = parseFloat(document.getElementById(`V${i}`).value) || 0;
    }

    return features;
}

/**
 * Display prediction results
 * @param {Object} r - Result object from the API
 */
function showResult(r) {
    const isFraud = r.result === 'FRAUD';

    result.className = 'result ' + (isFraud ? 'fraud' : 'legit');
    result.innerHTML = `
        <h3>${isFraud ? '🚨 FRAUD DETECTED' : '✅ LEGITIMATE TRANSACTION'}</h3>
        <p style="font-size: 16px; margin: 10px 0;"><strong>Risk Level:</strong> ${r.risk_level}</p>
        <div class="stats">
            <div class="stat">
                <div class="stat-label">Fraud Probability</div>
                <div class="stat-value" style="color: #ef4444;">${r.fraud_probability}%</div>
            </div>
            <div class="stat">
                <div class="stat-label">Legit Probability</div>
                <div class="stat-value" style="color: #10b981;">${r.legitimate_probability}%</div>
            </div>
            <div class="stat">
                <div class="stat-label">Confidence</div>
                <div class="stat-value">${Math.max(r.fraud_probability, r.legitimate_probability).toFixed(2)}%</div>
            </div>
        </div>
    `;
    result.style.display = 'block';
}

/**
 * Handle form submission
 */
form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const features = collectFeatures();

    // Update UI state
    btn.disabled = true;
    loading.style.display = 'block';
    result.style.display = 'none';

    try {
        // Send prediction request to backend
        const res = await fetch('/predict', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({features})
        });

        const data = await res.json();

        if (data.success) {
            showResult(data.result);
        } else {
            alert('Error: ' + data.error);
        }
    } catch (err) {
        alert('Error: ' + err.message);
    } finally {
        // Reset UI state
        btn.disabled = false;
        loading.style.display = 'none';
    }
});
