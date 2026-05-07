/**
 * BI Dashboard — Main JavaScript
 * Sidebar toggle + Chart.js initialization
 */

'use strict';

// ── Sidebar Toggle ──────────────────────────────────────────
const sidebar       = document.getElementById('sidebar');
const sidebarToggle = document.getElementById('sidebarToggle');

if (sidebarToggle && sidebar) {
    sidebarToggle.addEventListener('click', () => {
        const isMobile = window.innerWidth <= 768;
        if (isMobile) {
            sidebar.classList.toggle('mobile-open');
        } else {
            sidebar.classList.toggle('collapsed');
        }
    });
}

// ── Chart.js Global Defaults ────────────────────────────────
Chart.defaults.font.family = "'Inter', system-ui, sans-serif";
Chart.defaults.font.size   = 12;
Chart.defaults.color       = '#9ca3af';
Chart.defaults.plugins.legend.labels.boxWidth  = 12;
Chart.defaults.plugins.legend.labels.padding   = 16;
Chart.defaults.plugins.tooltip.padding         = 10;
Chart.defaults.plugins.tooltip.cornerRadius    = 8;
Chart.defaults.plugins.tooltip.backgroundColor = 'rgba(17, 24, 39, 0.9)';

// ── Color Palette ───────────────────────────────────────────
const COLORS = {
    primary:   '#6366f1',
    success:   '#10b981',
    warning:   '#f59e0b',
    danger:    '#ef4444',
    info:      '#06b6d4',
    purple:    '#8b5cf6',
    pink:      '#ec4899',
    palette: [
        '#6366f1', '#10b981', '#f59e0b',
        '#ef4444', '#06b6d4', '#8b5cf6',
        '#ec4899', '#14b8a6',
    ],
};

// ── Helper: format Rupiah untuk tooltip ────────────────────
function formatRupiah(value) {
    return 'Rp ' + new Intl.NumberFormat('id-ID').format(value);
}

// ── Dashboard Charts ────────────────────────────────────────
async function initDashboardCharts() {
    try {
        // Fetch semua data secara paralel
        const [monthly, category, region, topProducts] = await Promise.all([
            fetch('/api/sales-monthly').then(r => r.json()),
            fetch('/api/sales-by-category').then(r => r.json()),
            fetch('/api/sales-by-region').then(r => r.json()),
            fetch('/api/top-products').then(r => r.json()),
        ]);

        renderMonthlyChart(monthly);
        renderCategoryChart(category);
        renderRegionChart(region);
        renderTopProductsChart(topProducts);

    } catch (err) {
        console.error('Failed to load chart data:', err);
    }
}

// ── Chart 1: Monthly Revenue (Line) ────────────────────────
function renderMonthlyChart(data) {
    const ctx = document.getElementById('chartMonthly');
    if (!ctx) return;

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.labels,
            datasets: [{
                label: 'Revenue',
                data: data.revenue,
                borderColor: COLORS.primary,
                backgroundColor: 'rgba(99, 102, 241, 0.08)',
                borderWidth: 2.5,
                pointBackgroundColor: COLORS.primary,
                pointRadius: 4,
                pointHoverRadius: 6,
                fill: true,
                tension: 0.4,
            }],
        },
        options: {
            responsive: true,
            interaction: { mode: 'index', intersect: false },
            plugins: {
                legend: { display: false },
                tooltip: {
                    callbacks: {
                        label: ctx => ' ' + formatRupiah(ctx.parsed.y),
                    },
                },
            },
            scales: {
                x: {
                    grid: { display: false },
                    border: { display: false },
                },
                y: {
                    grid: { color: '#f3f4f6' },
                    border: { display: false, dash: [4, 4] },
                    ticks: {
                        callback: v => 'Rp ' + (v / 1_000_000).toFixed(0) + 'M',
                    },
                },
            },
        },
    });
}

// ── Chart 2: Category Doughnut ──────────────────────────────
function renderCategoryChart(data) {
    const ctx = document.getElementById('chartCategory');
    if (!ctx) return;

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: data.labels,
            datasets: [{
                data: data.revenue,
                backgroundColor: COLORS.palette,
                borderWidth: 2,
                borderColor: '#ffffff',
                hoverOffset: 6,
            }],
        },
        options: {
            responsive: true,
            cutout: '65%',
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: { padding: 12 },
                },
                tooltip: {
                    callbacks: {
                        label: ctx => ' ' + formatRupiah(ctx.parsed),
                    },
                },
            },
        },
    });
}

// ── Chart 3: Region Bar ─────────────────────────────────────
function renderRegionChart(data) {
    const ctx = document.getElementById('chartRegion');
    if (!ctx) return;

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.labels,
            datasets: [{
                label: 'Revenue',
                data: data.revenue,
                backgroundColor: COLORS.palette.map(c => c + '99'), // 60% opacity
                borderColor: COLORS.palette,
                borderWidth: 1.5,
                borderRadius: 6,
            }],
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: false },
                tooltip: {
                    callbacks: {
                        label: ctx => ' ' + formatRupiah(ctx.parsed.y),
                    },
                },
            },
            scales: {
                x: {
                    grid: { display: false },
                    border: { display: false },
                },
                y: {
                    grid: { color: '#f3f4f6' },
                    border: { display: false },
                    ticks: {
                        callback: v => 'Rp ' + (v / 1_000_000).toFixed(0) + 'M',
                    },
                },
            },
        },
    });
}

// ── Chart 4: Top Products Horizontal Bar ────────────────────
function renderTopProductsChart(data) {
    const ctx = document.getElementById('chartTopProducts');
    if (!ctx) return;

    // Potong nama produk yang terlalu panjang
    const labels = data.labels.map(l => l.length > 20 ? l.substring(0, 18) + '…' : l);

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Revenue',
                data: data.revenue,
                backgroundColor: COLORS.palette.slice(0, 5).map(c => c + 'bb'),
                borderColor: COLORS.palette.slice(0, 5),
                borderWidth: 1.5,
                borderRadius: 6,
            }],
        },
        options: {
            indexAxis: 'y',   // horizontal bar
            responsive: true,
            plugins: {
                legend: { display: false },
                tooltip: {
                    callbacks: {
                        label: ctx => ' ' + formatRupiah(ctx.parsed.x),
                    },
                },
            },
            scales: {
                x: {
                    grid: { color: '#f3f4f6' },
                    border: { display: false },
                    ticks: {
                        callback: v => 'Rp ' + (v / 1_000_000).toFixed(0) + 'M',
                    },
                },
                y: {
                    grid: { display: false },
                    border: { display: false },
                },
            },
        },
    });
}
