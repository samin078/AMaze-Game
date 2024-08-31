def get_membership_blocks_accessed(blocks_accessed, shortest_path_blocks,level):
    degree = {}
    percentage = (max(0, blocks_accessed - shortest_path_blocks) / shortest_path_blocks) * 100
    print(f'Block Percentage: {percentage}')
    if level == 'easy':
        if percentage>=0 and percentage<= 15:
            degree["low"] = 1
            degree["medium"] = 0
            degree["high"] = 0
        elif percentage>15 and percentage <= 20:
            degree["low"] = (20 - percentage) / (20-15)
            degree["medium"] = (percentage - 15) / (20-15)
            degree["high"] = 0
        elif percentage>20 and percentage <= 25:
            degree["low"] = 0
            degree["medium"] = (25 - percentage) / (25-20)
            degree["high"] = (percentage - 20) / (25-20)
        else:
            degree["low"] = 0
            degree["medium"] = 0
            degree["high"] = 1
    elif level == 'medium':
        if percentage>=0 and percentage<= 13:
            degree["low"] = 1
            degree["medium"] = 0
            degree["high"] = 0
        elif percentage>13 and percentage<= 17:
            degree["low"] = (17 - percentage) / (17-13)
            degree["medium"] = (percentage - 13) / (17-13)
            degree["high"] = 0
        elif percentage>17 and percentage<= 21:
            degree["low"] = 0
            degree["medium"] = (21 - percentage) / (21-17)
            degree["high"] = (percentage - 17) / (21-17)
        else:
            degree["low"] = 0
            degree["medium"] = 0
            degree["high"] = 1

    elif level == 'hard':
        if percentage>=0 and percentage<= 9:
            degree["low"] = 1
            degree["medium"] = 0
            degree["high"] = 0
        elif percentage>10 and percentage<= 13:
            degree["low"] = (13 - percentage) / (13-10)
            degree["medium"] = (percentage - 10) / (13-10)
            degree["high"] = 0
        elif percentage>13 and percentage<= 15:
            degree["low"] = 0
            degree["medium"] = (15 - percentage) / (15-13)
            degree["high"] = (percentage - 13) / (15-13)
        else:
            degree["low"] = 0
            degree["medium"] = 0
            degree["high"] = 1
    print(f'BLock degree: {degree}')
    return degree


def get_membership_time_elapsed(time_elapsed, optimal_path_length,level):
    degree = {}
    if level == 'easy':
        optimal_time = 0.6 * optimal_path_length
        print(f'Optimal_time: {optimal_time}')
    elif level == 'medium':
        optimal_time = 0.5 * optimal_path_length
        print(f'Optimal_time: {optimal_time}')
    elif level == 'hard':
        optimal_time = 0.48 * optimal_path_length
        print(f'Optimal_time: {optimal_time}')
    else:
        raise ValueError("Invalid level")
    
    percentage = (max(0, time_elapsed - optimal_time) / optimal_time) * 100
    print(f'Time Percentage: {percentage}')
    if level == 'easy':
        if percentage>=0 and percentage <= 10:
            degree["low"] = 1
            degree["medium"] = 0
            degree["high"] = 0
        elif percentage > 10 and percentage <= 15:
            degree["low"] = (15 - percentage) / (15-10)
            degree["medium"] = (percentage - 10) / (15-10)
            degree["high"] = 0
        elif percentage > 15 and percentage <= 20:
            degree["low"] = 0
            degree["medium"] = (20 - percentage) / (20-15)
            degree["high"] = (percentage - 15) / (20-15)
        else:
            degree["low"] = 0
            degree["medium"] = 0
            degree["high"] = 1

    elif level == 'medium':
        if percentage>=0 and percentage <= 8:
            degree["low"] = 1
            degree["medium"] = 0
            degree["high"] = 0
        elif percentage > 8 and percentage <= 12:
            degree["low"] = (12 - percentage) / (12-10)
            degree["medium"] = (percentage - 10) / (12-10)
            degree["high"] = 0
        elif percentage > 12 and percentage <= 16:
            degree["low"] = 0
            degree["medium"] = (16 - percentage) / (16-12)
            degree["high"] = (percentage - 12) / (16-12)
        else:
            degree["low"] = 0
            degree["medium"] = 0
            degree["high"] = 1
       
    elif level == 'hard':
        if percentage>=0 and percentage <= 5:
            degree["low"] = 1
            degree["medium"] = 0
            degree["high"] = 0
        elif percentage > 5 and percentage <= 8:
            degree["low"] = (8 - percentage) / (8-5)
            degree["medium"] = (percentage - 5) / (8-5)
            degree["high"] = 0
        elif percentage > 8 and percentage <= 11:
            degree["low"] = 0
            degree["medium"] = (11 - percentage) / (11-8)
            degree["high"] = (percentage - 8) / (11-8)
        else:
            degree["low"] = 0
            degree["medium"] = 0
            degree["high"] = 1
    print(f'Time degree: {degree}')
    return degree

def rule_evaluation(blocks, time):
    high = []
    medium = []
    low = []

    # Rule 1: Low score if blocks accessed is high and time elapsed is high
    rule1 = min(blocks["high"], time["high"])
    # Rule 2: Medium score if blocks accessed is medium and time elapsed is medium
    rule2 = min(blocks["medium"], time["medium"])
    # Rule 3: High score if blocks accessed is low and time elapsed is low
    rule3 = min(blocks["low"], time["low"])
    # Rule 4: Low score if blocks accessed is high and time elapsed is medium
    rule4 = min(blocks["high"], time["medium"])
    # Rule 5: Medium score if blocks accessed is medium and time elapsed is high
    rule5 = min(blocks["medium"], time["high"])
    # Rule 6: High score if blocks accessed is low and time elapsed is medium
    rule6 = min(blocks["low"], time["medium"])
    # Rule 7: High score if blocks accessed is medium and time elapsed is low
    rule7 = min(blocks["medium"], time["low"])
    # Rule 8: Low score if blocks accessed is high and time elapsed is low
    rule8 = min(blocks["high"], time["low"])
    # Rule 9: Medium score if blocks accessed is low and time elapsed is high
    rule9 = min(blocks["low"], time["high"])

    low.append((rule1 + rule4 + rule8)/3.0)
    medium.append((rule2 + rule5 + rule9)/3.0)
    high.append((rule3 + rule6 + rule7)/3.0)

    print(f'Low : {low}')
    print(f'Medium : {medium}')
    print(f'High : {high}')
    return low , medium , high

def defuzzify(low, medium, high):
     # Define centroid values for the output fuzzy sets
    high_centroid = 75
    medium_centroid = 50
    low_centroid = 25

    # Calculate the numerator of the defuzzification formula
    numerator = ( sum(low) * low_centroid + sum(medium) * medium_centroid +  sum(high) * high_centroid)
    # Calculate the denominator of the defuzzification formula
    denominator = ( sum(low) + sum(medium) + sum(high))
  
    if denominator == 0:
        return 0  # Avoid division by zero
    print(f'Crisp: {numerator / denominator}')
    return numerator / denominator
