document.addEventListener("DOMContentLoaded", function() {

    // GRAFICA BARRAS
    const barCanvas = document.getElementById('barChart');
    if (barCanvas) {
        const clientes = JSON.parse(barCanvas.dataset.clientes || '[]');
        const montos = JSON.parse(barCanvas.dataset.montos || '[]');
        if (Array.isArray(clientes) && clientes.length && Array.isArray(montos)) {
            const colors = clientes.map((_, i) => `hsl(${(i * 60) % 360}, 60%, 60%)`);
            new Chart(barCanvas.getContext('2d'), {
                type: 'bar',
                data: {
                    labels: clientes,
                    datasets: [{ label: 'Monto de créditos', data: montos, backgroundColor: colors }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: { display: false },
                        tooltip: { callbacks: { label: ctx => '$' + Number(ctx.raw).toLocaleString() } },
                        datalabels: { anchor: 'end', align: 'end', color: '#000', formatter: (v) => '$' + Number(v).toLocaleString() }
                    },
                    scales: { y: { beginAtZero: true, ticks: { callback: v => '$' + v } } }
                },
                plugins: [ChartDataLabels]
            });
        }
    }

    // GRAFICA PASTEL 
    const pieCanvas = document.getElementById('pieChart');
    const pieDataScript = document.getElementById('pie-data');
    if (pieCanvas && pieDataScript) {
        let payload = {};
        try { payload = JSON.parse(pieDataScript.textContent || '{}'); } catch (e) { payload = {}; }

        if (payload.labels && payload.data && Array.isArray(payload.labels) && Array.isArray(payload.data)) {
            const labels = payload.labels;
            const data = payload.data.map(x => Number(x) || 0);
            const total = data.reduce((a,b)=>a+b,0);

            if (total > 0) {
                const baseColors = ['#4271b3', '#315290', '#5a6ca0', '#6e7db8', '#8aa1c1', '#aac0e1'];
                const colors = data.map((_,i)=>baseColors[i%baseColors.length]);

                new Chart(pieCanvas.getContext('2d'), {
                    type: 'pie',
                    data: { labels, datasets:[{data, backgroundColor: colors}] },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: { position: 'bottom' },
                            datalabels: {
                                color: '#fff',
                                formatter: function(value) { return value>0 ? ((value/total*100).toFixed(1)+'%') : ""; },
                                font: { weight: 'bold', size: 12 }
                            }
                        }
                    },
                    plugins: [ChartDataLabels]
                });
            } else {
                const notice = document.createElement('div');
                notice.className='chart-notice';
                notice.textContent='No hay créditos suficientes para mostrar el gráfico de pastel.';
                if (pieCanvas.parentNode) pieCanvas.parentNode.insertBefore(notice,pieCanvas.nextSibling);
            }
        }
    }

    // MENSAJES
    const flashes = document.querySelectorAll(".flash");
    flashes.forEach(flash => {
        flash.classList.add("show");
        if (!flash.classList.contains("active_client")) {
            setTimeout(()=>{ flash.remove(); }, 3500);
        } else {
            const modal = document.getElementById('activeClientModal');
            const acceptBtn = document.getElementById('acceptModal');
            if(modal && acceptBtn) {
                modal.style.display = 'flex';
                acceptBtn.onclick = ()=>{ modal.style.display='none'; flash.remove(); };
            }
        }
    });
});
