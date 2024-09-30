### Your code ###
boat_side='Right'
missionaries_on_right=3
cannibals_on_right=3
missionaries_on_left=0
cannibals_on_left=0

print('M=',missionaries_on_left,'C=',cannibals_on_left,'|----B|','M=',missionaries_on_right,'C=',cannibals_on_right)
while True:
  missionaries=int(input('Enter number of missionries on Boat:'))
  cannibals=int(input('Enter number of cannibals on Boat:'))
  if not (missionaries+cannibals==1 or missionaries+cannibals==2):
    print('Invalid Move!')

    continue

  if (boat_side=='Right'):
      if (missionaries>missionaries_on_right or cannibals>cannibals_on_right):
        print('Invalid move 2')

        continue

      missionaries_on_right-=missionaries
      cannibals_on_right-=cannibals
      missionaries_on_left+=missionaries
      cannibals_on_left+=cannibals
      boat_side='Left'
      print('M=',missionaries_on_left,'C=',cannibals_on_left,'|B----|','M=',missionaries_on_right,'C=',cannibals_on_right)


  elif boat_side=='Left':

    if (missionaries>missionaries_on_left or cannibals>cannibals_on_left):
      print('Invalid Move 2')

      continue

    missionaries_on_left-=missionaries
    cannibals_on_left-=cannibals
    missionaries_on_right+=missionaries
    cannibals_on_right+=cannibals
    boat_side='Right'
    print('M=',missionaries_on_left,'C=',cannibals_on_left,'|----B|','M=',missionaries_on_right,'C=',cannibals_on_right)

  if (missionaries_on_right<cannibals_on_right and missionaries_on_right>0) or (missionaries_on_left<cannibals_on_left and missionaries_on_left>0):
    print('You LOSE!')
    break
  if (missionaries_on_left==3 and cannibals_on_left==3):
    print('You Win..!')
    break

