#!/usr/bin/node
const skinDiseases = [
  {
    name: 'Acne',
    symptoms: [
      'Pimples',
      'Whiteheads',
      'Blackheads',
      'Inflamed red bumps'
    ],
    diagnosis: 'Visual examination by a dermatologist',
    treatment: 'Topical creams, oral medications, lifestyle changes'
  },
  {
    name: 'Eczema',
    symptoms: [
      'Dry, sensitive skin',
      'Red, inflamed skin',
      'Itching',
      'Cracked, scaly skin'
    ],
    diagnosis: 'Clinical examination, patch testing, skin biopsy',
    treatment: 'Emollients, topical corticosteroids, antihistamines'
  },
  {
    name: 'Psoriasis',
    symptoms: [
      'Red patches of skin',
      'Thick, silvery scales',
      'Dry, cracked skin that may bleed',
      'Itching or burning sensation'
    ],
    diagnosis: 'Visual examination, skin biopsy',
    treatment: 'Topical treatments, phototherapy, systemic medications'
  }
];

console.log(skinDiseases);
