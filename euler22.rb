letters = ('a'..'z').to_a
letterValues = {}
letters.each_with_index do |letter, idx|
  letterValues[letter] = (idx + 1)
end

def name_score name, hsh = {}
  score = 0
  name.downcase.each_char do |char|
    score += hsh[char]
  end
  score
end

names = File.read('names.txt').split(',')

def list_score list, hsh={}
  list = list.sort
  score = 0
  list.each_with_index do |name, idx|
    score += name_score(name.gsub('"',''), hsh) * (idx+1)
  end
  score
end

puts list_score(names,letterValues)