"""Figure 2: method comparison on the UMUD benchmark. Print-safe grayscale."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": "serif", "font.serif": ["Times New Roman", "DejaVu Serif"],
    "font.size": 9, "axes.linewidth": 0.6, "xtick.major.width": 0.6,
    "pdf.fonttype": 42, "ps.fonttype": 42,          # embed real fonts, not outlines
})

# ordered worst -> best so the eye lands on the subject at the bottom
methods = ["SMA\n(earlier automated)", "DL_Track_US\n(field standard)",
           "Single human expert\n(leave-one-out median)", "This method"]
scores  = [0.409, 0.331, 0.264, 0.196]
# single hue, separated by lightness: unambiguous in grayscale and under any CVD
shades  = ["0.78", "0.62", "0.46", "0.18"]

fig, ax = plt.subplots(figsize=(5.4, 2.5))
bars = ax.barh(range(len(methods)), scores, height=0.62,
               color=shades, edgecolor="white", linewidth=1.2)   # 2px-equivalent surface gap

for i, (b, s) in enumerate(zip(bars, scores)):
    ax.text(b.get_width() + 0.008, b.get_y() + b.get_height()/2, f"{s:.3f}",
            va="center", ha="left", fontsize=9,
            fontweight="bold" if i == len(scores)-1 else "normal", color="0.15")

ax.set_yticks(range(len(methods)))
ax.set_yticklabels(methods, fontsize=8.5)
ax.invert_yaxis()
ax.set_xlabel("UMUD score against the seven-rater consensus  (lower is better)", fontsize=8.5)
ax.set_xlim(0, 0.46)
ax.xaxis.set_major_locator(plt.MultipleLocator(0.1))
ax.xaxis.grid(True, color="0.88", linewidth=0.5)     # recessive grid
ax.set_axisbelow(True)
for side in ("top", "right", "left"):
    ax.spines[side].set_visible(False)
ax.spines["bottom"].set_color("0.6")
ax.tick_params(axis="y", length=0)
ax.tick_params(axis="x", colors="0.4", labelsize=8)

fig.tight_layout(pad=0.4)
for ext in ("pdf", "png"):
    fig.savefig(f"figures/fig2_comparison.{ext}", dpi=600, bbox_inches="tight")
print("wrote figures/fig2_comparison.pdf and .png")
