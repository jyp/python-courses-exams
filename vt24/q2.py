
def gene_match(gene,genome_file):
  i = 0
  l = len(gene)
  with open(genome_file) as f:
    ref = f.read(l)
    while True:
      if ref == gene:
        print(i)
      c = f.read(1)
      if c:
        ref = ref[1:]+c
        i=i+1
      else:
        return

gene_match("ACA","genome.txt")
